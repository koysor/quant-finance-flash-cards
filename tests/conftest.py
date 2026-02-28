import pytest
import os
import sys
from pathlib import Path

# Add project root to path so 'app' can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app

@pytest.fixture
def app():
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
