# Docker Deployment Guide

## Architecture

The flash cards app is deployed on the shared EC2 instance alongside the quant-finance apps and maths-python. Caddy (managed by the quant-finance repository) provides automatic HTTPS via Let's Encrypt and routes `/flashcards/*` traffic to this container.

```
Internet (HTTPS :443)
    │
    ▼
Caddy Reverse Proxy (managed by quant-finance)
    │
    ├─► quant-finance:8501  (/quant/)
    ├─► options:8501        (/options/)
    ├─► fixed-income:8501   (/fixed-income/)
    ├─► portfolio:8501      (/portfolio/)
    ├─► host:8505           (/maths/)
    │
    └─► host:8506           (/flashcards/)
            │
            ▼
        flashcards container (gunicorn on internal port 8000)
```

Caddy uses `handle_path`, which strips `/flashcards` before proxying, and adds `X-Forwarded-Prefix: /flashcards`. The Flask app wraps itself in `ProxyFix` (`app/__init__.py`), which turns that header into `SCRIPT_NAME`, so every `url_for` link and the search-data fetch come out as `/flashcards/...`. Inside the container the app is served from `/`.

For the AWS side (instance, security groups, Elastic IP, cost, monitoring) see [`quant-finance/docker/AWS_CLOUD.md`](https://github.com/koysor/quant-finance/blob/main/docker/AWS_CLOUD.md).

## Local Development

Without Docker:

```bash
uv sync
FLASK_DEBUG=1 uv run python run.py      # http://127.0.0.1:5000
```

With Docker, from the repository root:

```bash
docker build -f docker/Dockerfile -t flashcards .
docker run --rm -p 8000:8000 -e SECRET_KEY=dev flashcards
```

Access at http://localhost:8000/. To check the prefix handling the way Caddy sends it:

```bash
curl -s -H 'X-Forwarded-Prefix: /flashcards' http://localhost:8000/ | grep -o 'href="/flashcards/[^"]*"' | head -3
```

## Production Deployment (EC2)

### How it works

1. A push to `main` starts the workflow in [`.github/workflows/deploy-ec2.yml`](../.github/workflows/deploy-ec2.yml) (see [`DEPLOY-EC2.md`](../.github/workflows/DEPLOY-EC2.md))
2. The `test` job runs `pytest`; the `build-and-push` job builds `docker/Dockerfile` and pushes `ghcr.io/koysor/quant-finance-flash-cards` (tagged with the commit SHA and `latest`)
3. The `deploy` job SSHes into EC2 as `ec2-user`, updates the clone in `~/quant-finance-flash-cards`, pulls the image and starts it with `docker-compose`
4. The container publishes host port 8506
5. Caddy (from quant-finance) routes `https://koysor.duckdns.org/flashcards/*` to `host.docker.internal:8506`

The image is built on GitHub's runners, not on the instance, because the t3.micro has too little RAM for builds.

### Docker Compose files

| File | Purpose |
|------|---------|
| `docker-compose.prod.yml` | Production (uses the pre-built GHCR image) |

There is no local compose file; use `docker build` and `docker run` as above.

### Runtime configuration

| Setting | Where | Value |
|---|---|---|
| `SECRET_KEY` | `docker/.env` on the host (read via `env_file`) | Required. 64 hex characters, never committed |
| `WEB_CONCURRENCY` | `docker-compose.prod.yml` | `1` gunicorn worker (`gunicorn.conf.py` default) |
| `GUNICORN_BIND` | unset | Defaults to `0.0.0.0:8000` |
| `ALLOW_EDGE_EDIT` | unset | Leave unset. It enables the remove-link button, which rewrites `edges.json`; the container's copy is not persisted |
| `mem_limit` / `memswap_limit` | `docker-compose.prod.yml` | `180m` / `256m`, the same as the other apps |

`graph.db` is derived data. It is rebuilt from `cards/` and `edges.json` every time the container starts (a few seconds), so there is no volume to back up. Card changes reach production by pushing to `main`.

### First-time host setup

Done once, over SSH as `ec2-user`. Order matters: the deploy job runs `git fetch` inside `~/quant-finance-flash-cards`, which fails if that directory exists but is not a clone.

```bash
git clone https://github.com/koysor/quant-finance-flash-cards.git ~/quant-finance-flash-cards
cd ~/quant-finance-flash-cards
mkdir -p docker && cd docker      # docker/ exists after the first push; harmless before

umask 077
printf 'SECRET_KEY=%s\n' "$(python3 -c 'import secrets; print(secrets.token_hex(32))')" > .env
chmod 600 .env
```

The deploy job stops with `docker/.env is missing` if the file is absent. `git reset --hard` leaves the untracked `.env` alone.

Also make the GHCR package public (GitHub → Packages → `quant-finance-flash-cards` → Package settings → Change visibility), because the host pulls without credentials.

### GitHub secrets and the deploy key

| Secret | Value |
|---|---|
| `EC2_HOST` | The instance's Elastic IP (see AWS_CLOUD.md) |
| `EC2_SSH_KEY` | Private key for `ec2-user` on the instance |

This repo uses its own ed25519 deploy key, separate from the key the other repos use, so it can be rotated independently. To create or rotate it:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/flashcards_deploy -N "" -C "flashcards-github-deploy"

# On the instance (console session or an existing key): append the PUBLIC half
echo '<contents of ~/.ssh/flashcards_deploy.pub>' >> ~/.ssh/authorized_keys

# Store the PRIVATE half as the secret and check the login
gh secret set EC2_SSH_KEY --repo koysor/quant-finance-flash-cards < ~/.ssh/flashcards_deploy
ssh -i ~/.ssh/flashcards_deploy ec2-user@<EC2_HOST> 'echo ok'
```

Append with `>>` so the other keys keep working. When rotating, remove the old public key's line from `authorized_keys` afterwards. Keep a backup of the private key somewhere safe; GitHub never shows a stored secret again.

### Manual deployment

```bash
# SSH into EC2
cd ~/quant-finance-flash-cards/docker

docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d
docker logs -f flashcards-flashcards-1
```

### Updating

Normally just push to `main`. By hand:

```bash
cd ~/quant-finance-flash-cards
git fetch origin && git reset --hard origin/main
cd docker
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d
```

## Port Allocation on Shared EC2

```
Host Port    Container Port    App                  Repository
─────────    ──────────────    ─────────────────    ──────────────
8501         8501              quant-finance        quant-finance
8502         8501              options              quant-finance
8503         8501              fixed-income         quant-finance
8504         8501              portfolio-management quant-finance
8505         8501              maths-python         maths-python
8506         8000              flashcards           quant-finance-flash-cards
```

## HTTPS and Shared-Host Coupling

HTTPS is provided by Caddy in the quant-finance deployment. The Caddyfile entry (in `quant-finance/docker/Caddyfile`):

```
redir /flashcards /flashcards/ permanent

handle_path /flashcards/* {
    reverse_proxy host.docker.internal:8506 {
        header_up X-Forwarded-Prefix /flashcards
    }
}
```

- The flashcards container publishes port 8506 on the EC2 host; Caddy terminates TLS and proxies to it
- Certificate renewal is handled by Caddy; this repo does nothing for TLS
- The quant-finance deploy runs `docker system prune -af`, which deletes this app's image because it runs in a separate compose project. The quant-finance workflow therefore re-pulls and restarts flashcards after pruning, and health-checks it. Both steps only run when `~/quant-finance-flash-cards/docker/.env` exists
- The bare site root (`/`) redirects to `/quant/`; that is also configured in the quant-finance Caddyfile

## Capacity

The instance is a 1 GiB t3.micro shared by Caddy and five other containers, with a 1 GB swapfile. Measured on 18 October 2026:

| | Value |
|---|---|
| App footprint, 1 worker (local, after hitting the heaviest pages) | about 107 MB |
| `docker stats` on the instance shortly after deploy | 96 MiB of the 180 MiB cap |
| Instance before deploying this app | 550 MB used, 219 MB available, 86 MB swap used |
| Instance just after | 567 MB used, 200 MB available, 166 MB swap used |

The index, graph and formulas pages are 1.6–2.3 MB of HTML each, which is what drives memory spikes. Keep `WEB_CONCURRENCY=1`. Check `free -m` and `docker stats --no-stream` now and then; if swap use keeps climbing or a container restarts, move the instance to a t3.small (2 GiB).

## Troubleshooting

| Symptom | Likely cause and fix |
|---|---|
| Deploy fails at `docker pull` with `denied` or `unauthorized` | The GHCR package is still private. Make it public, then re-run the workflow |
| Deploy stops with `docker/.env is missing` | Create `docker/.env` as in First-time host setup, then re-run |
| Deploy fails at `git fetch` with `not a git repository` | `~/quant-finance-flash-cards` exists without a clone. Remove it (keep `docker/.env` aside) and clone again |
| `/flashcards/` returns 404 from Caddy | The Caddy route is not deployed yet. Push the quant-finance repo |
| `/flashcards/` returns 502 | The container is down or still starting. `docker ps`, `docker logs flashcards-flashcards-1` |
| Pages load but links or search point at `/...` without the prefix | `ProxyFix` is not active, Caddy is not sending `X-Forwarded-Prefix`, or a template has a hardcoded root-relative URL. Use `url_for` |
| Container restarts repeatedly | Check `docker logs`. `SECRET_KEY must be set` means `docker/.env` is missing or empty; otherwise look for an out-of-memory kill (`docker inspect` shows `OOMKilled`) |
| SSH step: `Permission denied (publickey)` | The public key is not in `authorized_keys` on the instance, or `EC2_SSH_KEY` holds the wrong key |
| SSH step: `i/o timeout` | The instance is stopped. See "Stopped instance" in AWS_CLOUD.md |

For Caddy, disk space and general Docker problems see [`quant-finance/docker/TROUBLESHOOTING.md`](https://github.com/koysor/quant-finance/blob/main/docker/TROUBLESHOOTING.md).

## Live URL

https://koysor.duckdns.org/flashcards/
