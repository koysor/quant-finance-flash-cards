# Deploy to EC2 Workflow Explained

This documents [`deploy-ec2.yml`](deploy-ec2.yml). For the architecture, host setup and troubleshooting see [`docker/README.md`](../../docker/README.md).

## Overview

```
test ──► build-and-push ──► deploy (SSH ──► health check ──► summary)
```

Each job needs the previous one, so a failing test stops the build and nothing is pushed or deployed.

## Triggers

| Event | Behaviour |
|---|---|
| Push to `main` | Runs everything, including the deploy |
| Pull request to `main` | Runs `test` and builds the image without pushing it; no deploy |
| `workflow_dispatch` | Manual run from the Actions tab; use it to re-run after fixing the host |

## Job 1: test

Installs uv (`astral-sh/setup-uv`), runs `uv sync --locked` and `uv run pytest -q` with a dummy `SECRET_KEY`, since `create_app()` refuses to start without one. The tests use temporary copies of the database and `edges.json`, so they never touch repository data.

## Job 2: build-and-push

Builds `docker/Dockerfile` with Buildx and pushes to GitHub Container Registry using the built-in `GITHUB_TOKEN` (the job has `packages: write`). Images are tagged with the commit SHA and, on the default branch, `latest`. The layer cache is kept in the GitHub Actions cache. The package must be public so the host can pull without logging in.

## Job 3: deploy

Runs only for pushes and manual runs. It uses `appleboy/ssh-action` to connect to the instance as `ec2-user` and then:

1. Clones `~/quant-finance-flash-cards` if missing, otherwise `git fetch` and `git reset --hard origin/main` (this supplies `docker-compose.prod.yml`)
2. Aborts with a clear message if `docker/.env` does not exist
3. Stops the running container with `docker-compose down`
4. Runs `docker system prune -f`. It never uses `--volumes`, because Caddy's certificates live in a volume
5. Pulls `ghcr.io/koysor/quant-finance-flash-cards:latest` and starts it with `docker-compose up -d`

### Health check

A second SSH step waits 30 seconds, confirms the container is listed by `docker-compose ps`, and runs `curl -f http://localhost:8000/` inside it. The final step prints the public URL, `https://koysor.duckdns.org/flashcards/`.

## Secrets required

| Secret | Description |
|---|---|
| `EC2_HOST` | The instance's public (Elastic) IP |
| `EC2_SSH_KEY` | This repo's private deploy key for `ec2-user` |
| `GITHUB_TOKEN` | Provided automatically; used to push to GHCR |

How the deploy key is created and rotated is in [`docker/README.md`](../../docker/README.md#github-secrets-and-the-deploy-key).

## Common modifications

- **Change the port:** edit `docker/docker-compose.prod.yml` and the `reverse_proxy` target in the quant-finance Caddyfile together.
- **Change the deployment branch:** edit `on.push.branches` and `on.pull_request.branches`.
- **Add a build step or check:** add it to `test` (or a new job before `build-and-push`) so a failure blocks the deploy.
- **The quant-finance workflow:** it also restarts this container after its own `docker system prune -af`. If you rename the compose project, service or directory, update the flashcards block in `quant-finance/.github/workflows/deploy-ec2.yml` too.
