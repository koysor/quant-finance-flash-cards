import multiprocessing

# Bind to localhost only — nginx sits in front.
bind = "127.0.0.1:8000"

# sync workers are correct for SQLite (CPU-bound reads, no async I/O needed).
# Start with 2*nproc+1; tune down if memory is tight.
workers      = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"

# Load the app once in the master process, then fork.
# Workers share read-only memory (CoW) for card content and config dicts.
preload_app = True

# Kill a hung worker after 30 s rather than accumulating stuck requests.
timeout   = 30
keepalive = 5

accesslog = "/var/log/flashcards/access.log"
errorlog  = "/var/log/flashcards/error.log"
loglevel  = "info"
