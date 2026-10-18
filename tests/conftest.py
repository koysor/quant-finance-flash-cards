"""Shared pytest fixtures for the flash card application."""
import pytest
import os
import sys
from pathlib import Path

# Add project root to path so 'app' can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app

# create_app() refuses to start without SECRET_KEY unless FLASK_DEBUG is on.
os.environ.setdefault("SECRET_KEY", "test-secret-key")

@pytest.fixture(scope="session")
def _template_db(tmp_path_factory):
    """Build graph.db once per session; each test copies it."""
    import app.db as db
    path = tmp_path_factory.mktemp("template") / "graph.db"
    original = db.DB_PATH
    db.DB_PATH = path
    try:
        create_app()
    finally:
        db.DB_PATH = original
    return path


@pytest.fixture
def app(tmp_path, monkeypatch, _template_db):
    # Isolate writable state: tests must never touch the real graph.db or edges.json.
    import shutil
    import app.db as db
    edges = tmp_path / "edges.json"
    shutil.copy(db.EDGES_PATH, edges)
    shutil.copy(_template_db, tmp_path / "graph.db")
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "graph.db")
    monkeypatch.setattr(db, "EDGES_PATH", edges)
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # Use a dummy resources config if not present
    if "RESOURCES" not in app.config:
        app.config["RESOURCES"] = {}
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
