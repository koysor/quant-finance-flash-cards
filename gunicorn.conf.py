import os

# Inside the container Caddy reaches us over the Docker host port mapping, so
# bind to all interfaces; override with GUNICORN_BIND for a bare-metal setup.
bind = os.environ.get("GUNICORN_BIND", "0.0.0.0:8000")

# sync workers are correct for SQLite (CPU-bound reads, no async I/O needed).
# Default to one worker: the production host is a shared 1 GiB instance.
workers      = int(os.environ.get("WEB_CONCURRENCY", 1))
worker_class = "sync"

# Load the app once in the master process, then fork.
# Workers share read-only memory (CoW) for card content and config dicts.
preload_app = True

# Kill a hung worker after 30 s rather than accumulating stuck requests.
timeout   = 30
keepalive = 5

# Log to stdout/stderr so `docker logs` (or journald) captures everything.
accesslog = "-"
errorlog  = "-"
loglevel  = "info"
