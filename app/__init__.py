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
7. Register the main Blueprint and a context processor that injects template globals.
"""
import json
import os
import secrets
from typing import Any

from flask import Flask, render_template, session
from werkzeug.exceptions import HTTPException

from app.db import init_db, load_edges_from_file, get_all_cards, get_site_stats
from app.loader import load_all_cards
from app.routes import bp, TOPIC_COLOURS, _topic_colour


def _load_json_config(path: str, default: Any) -> Any:
    """Load a JSON file and return its contents, or *default* if the file is absent."""
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
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
    # SECRET_KEY must be stable across restarts in production to keep sessions valid.
    app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

    init_db()

    # notation.json maps LaTeX commands (e.g. "\sigma") to {symbol, meaning} pairs.
    # Used at card-load time to annotate which LaTeX symbols appear in each card.
    root = os.path.dirname(app.root_path)
    app.config["NOTATION"]  = _load_json_config(os.path.join(root, "notation.json"),  {})

    # key-terms.json maps plain variable names (e.g. "dW", "S") to {symbol, meaning} pairs.
    # Used at card-load time to annotate which equation variables appear in each card.
    app.config["KEY_TERMS"] = _load_json_config(os.path.join(root, "key-terms.json"), {})

    load_all_cards(
        app,
        notation_dict=app.config["NOTATION"],
        key_terms_dict=app.config["KEY_TERMS"],
    )
    load_edges_from_file()

    # resources.json maps card IDs to {websites, videos} lists shown in the sidebar.
    app.config["RESOURCES"] = _load_json_config(os.path.join(root, "resources.json"), {})

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
        site_stats
            Dict with ``card_count``, ``topic_count``, and ``edge_count``.
        csrf_token
            A per-session random hex token checked on every POST request.
        """
        cards = get_all_cards()
        stats = get_site_stats()
        search_data = json.dumps([
            {
                "id":     c["id"],
                "name":   c["name"],
                "topic":  c["topic"],
                "tags":   c["tags"],
                "url":    f"/card/{c['id']}",
                "colour": _topic_colour(c["topic"]),
            }
            for c in cards
        ])
        if "csrf_token" not in session:
            session["csrf_token"] = secrets.token_hex(16)

        return {
            "topic_colour":     _topic_colour,
            "search_data_json": search_data,
            "TOPIC_COLOURS":    TOPIC_COLOURS,
            "site_stats":       stats,
            "csrf_token":       session["csrf_token"],
        }

    @app.errorhandler(404)
    def not_found(e: HTTPException) -> tuple[str, int]:
        """Render the custom 404 page for any unmatched route."""
        return render_template("404.html"), 404

    return app
