import os

# Inside the container Caddy reaches us over the Docker host port mapping, so
# bind to all interfaces; override with GUNICORN_BIND for a bare-metal setup.
bind = os.environ.get("GUNICORN_BIND", "0.0.0.0:8000")

# gthread: each worker serves several requests at once, so one slow request or
# slow client no longer blocks everyone else.  Threads share the worker's memory
# (and its page cache), unlike extra workers.  SQLite connections are opened per
# request, so threads never share one.
# Default to one worker with two threads: the production host is a shared
# 1 GiB instance and the container is capped at 180 MB.  Each thread can be
# rendering a 2 MB page at once while the page cache is still cold after a
# restart, so raise GUNICORN_THREADS only with memory to spare.
workers = int(os.environ.get("WEB_CONCURRENCY", 1))
worker_class = "gthread"
threads = int(os.environ.get("GUNICORN_THREADS", 2))

# Load the app once in the master process, then fork.
# Workers share read-only memory (CoW) for card content and config dicts.
preload_app = True


def when_ready(server):
    """
    Runs in the master after the app has loaded and before workers fork.
    Startup (card parsing, the 32 MB SQLite bulk-load cache, cache warm-up)
    leaves freed memory that glibc keeps; hand it back to the OS so neither
    the master nor the forked workers carry it.
    """
    import ctypes
    import gc

    gc.collect()
    try:
        ctypes.CDLL("libc.so.6").malloc_trim(0)
    except OSError, AttributeError:
        pass  # not glibc (macOS, musl): nothing to trim


# Kill a hung worker after 30 s rather than accumulating stuck requests.
timeout = 30
keepalive = 5

# Log to stdout/stderr so `docker logs` (or journald) captures everything.
accesslog = "-"
errorlog = "-"
loglevel = "info"
