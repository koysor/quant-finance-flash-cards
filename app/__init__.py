"""
Application factory for the Quantitative Finance Flash Cards web app.

Startup sequence
----------------
1. ``init_db()``            — create the SQLite schema if it does not exist.
2. Load ``notation.json``   — LaTeX command definitions stored in app.config["NOTATION"].
3. Load ``key-terms.json``  — plain variable definitions stored in app.config["KEY_TERMS"].
4. ``load_all_cards()``     — scan ``cards/**/*.md``, upsert changed cards, remove stale ones.
5. ``load_edges_from_file()`` — repopulate the edges table from ``edges.json``.
6. Load ``resources.json``  — per-card learning links stored in app.config["RESOURCES"].
7. Register the main Blueprint and a context processor that injects template globals
   (the CSRF token only in edge-edit mode, so ordinary pages set no cookie).
8. Attach the HTTP caching hook (``Cache-Control`` and a weak ETag on GET 200s) and
   ``?v=<hash>`` versioning of ``url_for('static', ...)`` URLs.

Templates are dedented at compile time by ``_DedentTemplates``.  Page caching
itself is ``cached_page`` in ``app/routes.py``; ARCHITECTURE.md describes the design.
"""

import hashlib
import json
import os
import re
import secrets
from typing import Any

from flask import Flask, Response, g, render_template, request, session
from jinja2.ext import Extension
from werkzeug.exceptions import HTTPException
from werkzeug.middleware.proxy_fix import ProxyFix

from app.db import bulk_connection, init_db, load_edges_from_file, get_site_stats
from app.extensions import cache, edge_edit_enabled, limiter
from app.loader import load_all_cards
from app.routes import bp, TOPIC_COLOURS, _topic_colour, static_build, topic_slug


class _DedentTemplates(Extension):
    """
    Strip the leading indentation from every template source line before Jinja
    compiles it.  Newlines stay, so whitespace between tokens never disappears
    and rendering is unchanged.  Only template source is touched: card HTML
    inserted through variables (including ``<pre>`` code blocks) is not.  Do not
    put whitespace-sensitive content (``<pre>``, ``<textarea>``) directly in a
    template.
    """

    def preprocess(
        self, source: str, name: str | None, filename: str | None = None
    ) -> str:
        return _INDENT_RE.sub("", source)


_INDENT_RE = re.compile(r"^[ \t]+", re.MULTILINE)

_site_stats_cache: dict[str, int] | None = None


def _invalidate_global_cache() -> None:
    global _site_stats_cache
    _site_stats_cache = None


def _get_site_stats() -> dict[str, int]:
    global _site_stats_cache
    if _site_stats_cache is None:
        _site_stats_cache = get_site_stats()
    return _site_stats_cache


def _load_json_config(path: str, default: Any) -> Any:
    """Load a JSON file and return its contents, or *default* if the file is absent."""
    if os.path.exists(path):
        try:
            with open(path) as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Malformed JSON in {path}: {e}") from e
    return default


def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Reads the three committed data sources (``notation.json``, ``key-terms.json``,
    ``resources.json``), synchronises the SQLite cache with the card files on disk,
    and registers all routes and template helpers.

    Returns
    -------
    Flask
        A fully initialised application instance ready to serve requests.
    """
    app = Flask(__name__)
    # Template indentation was over a third of the large pages (730 KB of the
    # 2 MB index), all of it held in the page cache.  Drop it at compile time.
    # Not trim_blocks: removing the newline after a block tag can join tokens
    # once the next line's indentation is gone (``</span>{% endif %}`` then
    # ``</a>`` would render ``</span></a>``, dropping a space).
    app.jinja_env.add_extension(_DedentTemplates)
    # Behind Caddy: trust one proxy hop for client IP, scheme, host and the
    # X-Forwarded-Prefix header (the app is served under /flashcards/).
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    secret = os.environ.get("SECRET_KEY")
    if not secret and not app.debug:
        raise RuntimeError(
            "SECRET_KEY environment variable must be set in production. "
            "Run with FLASK_DEBUG=1 for local development."
        )
    app.secret_key = secret or secrets.token_hex(32)

    root = os.path.dirname(app.root_path)

    cache.init_app(
        app,
        config={
            "CACHE_TYPE": os.environ.get("CACHE_TYPE", "SimpleCache"),
            "CACHE_DEFAULT_TIMEOUT": 300,
            # SimpleCache entry cap.  A full cache of card and study-path pages
            # is about 20-30 MB; lower this if the container runs short.
            "CACHE_THRESHOLD": int(os.environ.get("CACHE_THRESHOLD", 500)),
            "CACHE_REDIS_URL": os.environ.get("REDIS_URL"),
        },
    )
    app.config.setdefault(
        "RATELIMIT_STORAGE_URI",
        os.environ.get("RATELIMIT_STORAGE_URI", "memory://"),
    )
    limiter.init_app(app)

    init_db()

    # notation.json maps LaTeX commands (e.g. "\sigma") to {symbol, meaning} pairs.
    # Used at card-load time to annotate which LaTeX symbols appear in each card.
    app.config["NOTATION"] = _load_json_config(os.path.join(root, "notation.json"), {})

    # key-terms.json maps plain variable names (e.g. "dW", "S") to {symbol, meaning} pairs.
    # Used at card-load time to annotate which equation variables appear in each card.
    app.config["KEY_TERMS"] = _load_json_config(
        os.path.join(root, "key-terms.json"), {}
    )

    with bulk_connection():
        load_all_cards(
            app,
            notation_dict=app.config["NOTATION"],
            key_terms_dict=app.config["KEY_TERMS"],
        )
        load_edges_from_file()
    _invalidate_global_cache()
    with app.app_context():
        cache.clear()  # evict any stale cached responses from a previous run

    # resources.json maps card IDs to {websites, videos} lists shown in the sidebar.
    app.config["RESOURCES"] = _load_json_config(
        os.path.join(root, "resources.json"), {}
    )

    @app.teardown_appcontext
    def close_db(exc: BaseException | None = None) -> None:
        conn = g.pop("db", None)
        if conn is not None:
            conn.close()

    app.register_blueprint(bp)

    @app.context_processor
    def inject_globals() -> dict[str, Any]:
        """
        Inject variables available in every template.

        Injected names
        --------------
        topic_colour(topic)
            Callable — returns the hex colour string for a given topic name.
        search_data_json
            JSON string of all cards (id, name, topic, tags, url, colour) for
            the client-side search box.
        TOPIC_COLOURS
            The full topic → colour mapping, used by the graph legend and filters.
        topic_slug(topic)
            Callable — the URL slug for ``/topic/<slug>`` and ``/quiz/<slug>``.
        static_build
            True while ``scripts/build_static.py`` renders the site to files.
        site_stats
            Dict with ``card_count``, ``topic_count``, and ``edge_count``.
        csrf_token
            A per-session random hex token checked on every POST request.
            Only created when edge editing is on; otherwise empty, so pages
            set no session cookie and shared caches can store them.
        """
        edit = edge_edit_enabled()
        if edit and "csrf_token" not in session:
            session["csrf_token"] = secrets.token_hex(16)

        return {
            "topic_colour": _topic_colour,
            "topic_slug": topic_slug,
            "static_build": static_build(),
            "TOPIC_COLOURS": TOPIC_COLOURS,
            "site_stats": _get_site_stats(),
            "csrf_token": session.get("csrf_token", "") if edit else "",
            "edge_edit_enabled": edit,
        }

    static_versions: dict[tuple[str, float], str] = {}

    @app.url_defaults
    def version_static_urls(endpoint: str, values: dict[str, Any]) -> None:
        """
        Add ``?v=<content hash>`` to every ``url_for('static', ...)`` URL, so
        static files can be cached for a year and still change on deploy.
        Keyed on mtime too, so an edited file gets a new hash in development.
        """
        if endpoint != "static" or "filename" not in values or not app.static_folder:
            return
        path = os.path.join(app.static_folder, values["filename"])
        try:
            key = (path, os.path.getmtime(path))
        except OSError:
            return
        if key not in static_versions:
            with open(path, "rb") as f:
                static_versions[key] = hashlib.sha256(f.read()).hexdigest()[:12]
        values["v"] = static_versions[key]

    # Every page is a pure function of the files loaded at startup, so one
    # token per start serves as the ETag: a restart or deploy changes it.
    build_id = secrets.token_hex(8)

    @app.after_request
    def add_cache_headers(response: Response) -> Response:
        """
        Set caching headers on successful GET responses.

        - Versioned static files (``?v=``): cached for a year.
        - Pages: ``Cache-Control: public, max-age=300`` unless the view set its
          own, plus a weak ETag, so browsers and shared caches (Caddy, a CDN)
          keep them and revalidate with a 304 instead of re-downloading.

        Pages are skipped in debug mode and in edge-edit mode, where they carry a
        per-session CSRF token.  Outside edit mode nothing writes to the session,
        so no page sets a cookie.  (The mode is checked rather than
        ``session.accessed``: in Flask 3.1 merely touching the ``session`` proxy
        marks it accessed and adds ``Vary: Cookie``.  Checking ``Set-Cookie``
        here would not work either: Flask adds the session cookie after these
        hooks run.)
        """
        if request.method != "GET" or response.status_code != 200:
            return response
        if request.endpoint == "static":
            if request.args.get("v"):
                response.headers["Cache-Control"] = (
                    "public, max-age=31536000, immutable"
                )
            return response
        if app.debug or edge_edit_enabled():
            return response
        response.headers.setdefault("Cache-Control", "public, max-age=300")
        response.set_etag(f"{build_id}-{response.mimetype}", weak=True)
        return response.make_conditional(request)

    @app.errorhandler(404)
    def not_found(e: HTTPException) -> tuple[str, int]:
        """Render the custom 404 page for any unmatched route."""
        return render_template("404.html"), 404

    return app
