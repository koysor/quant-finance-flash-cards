# Dockerfile for the Quant Finance Flash Cards Flask app
# syntax=docker/dockerfile:1

# Stage 1: Builder - install dependencies
FROM python:3.14-slim-bookworm AS builder

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv venv /opt/venv && \
    . /opt/venv/bin/activate && \
    uv export --no-dev --no-hashes --no-emit-project --format requirements-txt > requirements.txt && \
    uv pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.14-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1

COPY app/ ./app/
COPY cards/ ./cards/
COPY edges.json resources.json notation.json key-terms.json wsgi.py gunicorn.conf.py ./

# graph.db is derived from cards/ and edges.json and is rebuilt at startup,
# so /app must be writable by the runtime user.
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl --fail http://localhost:8000/ || exit 1

CMD ["gunicorn", "-c", "gunicorn.conf.py", "wsgi:app"]
