# Deploying the flash cards

The live site, https://koysor.duckdns.org/flashcards/, is a set of static files. [`deploy-ec2.yml`](deploy-ec2.yml) renders every page with the Flask app at build time and copies the result to the shared EC2 instance. Caddy, which belongs to the `quant-finance` repo, serves the files there directly. No Python runs on the server.

```
Internet (HTTPS :443)
    │
    ▼
Caddy (quant-finance/docker/Caddyfile)
    ├─► quant-finance, options, fixed-income, portfolio, maths-python containers
    └─► /flashcards/*  file_server  ~/flashcards-site/current   (mounted read-only)
```

## Workflow

```
test ──► static-build ──► publish-static (SSH upload ──► live check)
```

| Event | Behaviour |
|---|---|
| Push to `main` | Runs everything, including the publish |
| Pull request to `main` | Runs `test` and `static-build`, so a broken link fails the PR; no publish |
| `workflow_dispatch` | Manual run from the Actions tab |

Runs on the same branch are queued, never run in parallel (`concurrency`), so two publishes cannot prune each other's release.

### test

`uv sync --locked`, then `uv run pytest -q` with a dummy `SECRET_KEY`, since `create_app()` refuses to start without one. The tests use temporary copies of the database and `edges.json`.

### static-build

Runs `scripts/build_static.py --prefix /flashcards --out dist` (logic in `app/static_site.py`) and uploads `dist` as a tarball artifact. The build:

- requests every page through the Flask test client with `X-Forwarded-Prefix: /flashcards`, so `url_for` puts the prefix on every link;
- writes `/a/b` as `a/b.html`, `/` as `index.html`, plus `404.html`, `recent.json`, `search-data.json` and a copy of `app/static/`;
- fails if a page does not return 200, or if any page links to a file it did not write.

It takes about a minute and produces about 7,450 pages (about 220 MB, a 22 MB tarball). It has to run on Linux, because tags such as `P(A|B)` are not valid Windows file names. Locally, use WSL.

### publish-static

Push and manual runs only. It writes the `EC2_SSH_KEY` secret and an `ec2` host alias to `~/.ssh/config` and uses the runner's own `ssh`. It doesn't use `appleboy/ssh-action`, which downloads a binary from GitHub releases on every run. Over one SSH connection it then:

1. streams the tarball into `~/flashcards-site/releases/<sha>.tmp`, then renames it to `releases/<sha>`;
2. repoints `~/flashcards-site/current` at it in one rename (`ln -sfn` + `mv -T`). The link target is relative, so it also resolves inside the Caddy container;
3. deletes all but the three newest releases, never the live one;
4. removes the old gunicorn container and its image if they are still there (a no-op once gone).

A final step fetches `/flashcards/`, `/flashcards/graph` and a card page over HTTPS.

## Caddy

The `/flashcards/` block in `quant-finance/docker/Caddyfile`:

- serves files from `/srv/flashcards-site/current`, trying `{path}`, then `{path}.html`;
- returns 404 for directory URLs other than the root, and answers every 404 with the site's `404.html`. Its script also resolves bare `/flashcards/card/<slug>` links;
- sends `Cache-Control: public, max-age=300` on pages and a year on `/static/*`; `file_server` adds the ETag and Last-Modified;
- compresses with the site-wide `encode zstd gzip`. It does not use `precompressed`, because with Caddy 2.10 that answers ordinary requests with 206 Partial Content.

The quant-finance compose file mounts `${HOME}/flashcards-site` into Caddy read-only, and its deploy creates the directory first so Docker does not create it owned by root. A new release needs no Caddy reload. If you change the directory or the URL layout, change both repos.

## Rolling back

Point `current` at an earlier release on the instance. It takes effect immediately:

```bash
ls -1t ~/flashcards-site/releases/
cd ~/flashcards-site && ln -sfn releases/<sha> current.tmp && mv -T current.tmp current
```

The next push to `main` publishes over it again.

## Secrets

| Secret | Value |
|---|---|
| `EC2_HOST` | The instance's Elastic IP |
| `EC2_SSH_KEY` | This repo's private deploy key for `ec2-user` |

This repo has its own ed25519 deploy key, separate from the other repos' keys, so it can be rotated on its own:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/flashcards_deploy -N "" -C "flashcards-github-deploy"

# On the instance: append the PUBLIC half
echo '<contents of ~/.ssh/flashcards_deploy.pub>' >> ~/.ssh/authorized_keys

# Store the PRIVATE half as the secret and check the login
gh secret set EC2_SSH_KEY --repo koysor/quant-finance-flash-cards < ~/.ssh/flashcards_deploy
ssh -i ~/.ssh/flashcards_deploy ec2-user@<EC2_HOST> 'echo ok'
```

Append with `>>` so the other keys keep working. When rotating, remove the old public key's line from `authorized_keys` afterwards.

For the instance itself (security groups, Elastic IP, cost, monitoring) see [`quant-finance/docker/AWS_CLOUD.md`](https://github.com/koysor/quant-finance/blob/main/docker/AWS_CLOUD.md).
