"""Flash card web application factory."""
import json
import os
import secrets

from flask import Flask, render_template, session

from app.db import init_db, load_edges_from_file, get_all_cards, get_site_stats
from app.loader import load_all_cards
from app.routes import bp, TOPIC_COLOURS, _topic_colour


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

    init_db()
    load_all_cards(app)
    load_edges_from_file()

    resources_path = os.path.join(os.path.dirname(app.root_path), "resources.json")
    if os.path.exists(resources_path):
        with open(resources_path) as f:
            app.config["RESOURCES"] = json.load(f)
    else:
        app.config["RESOURCES"] = {}

    app.register_blueprint(bp)

    @app.context_processor
    def inject_globals():
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
    def not_found(e):
        return render_template("404.html"), 404

    return app
