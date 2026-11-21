"""How pages are rendered: URL prefix, static asset URLs, cookies, database
connections and template dedenting.  The static build renders every page this
way, so these properties are what the live site gets."""

import pytest

CARD = "/card/derivatives/black-scholes-equation"
PREFIX = {"X-Forwarded-Prefix": "/flashcards"}


@pytest.fixture(autouse=True)
def _no_edit(monkeypatch):
    monkeypatch.delenv("ALLOW_EDGE_EDIT", raising=False)


@pytest.fixture
def edit_enabled(monkeypatch):
    monkeypatch.setenv("ALLOW_EDGE_EDIT", "1")


def test_pages_set_no_cookie(client):
    for url in ("/", CARD, "/quiz", "/graph", "/recent"):
        resp = client.get(url)
        assert resp.status_code == 200, url
        assert "Set-Cookie" not in resp.headers, url


def test_links_follow_the_forwarded_prefix(client):
    # Card links appear as href="..." in pages and as "url": "..." in /graph's JSON.
    for url in ("/", CARD, "/graph"):
        bare = client.get(url).get_data(as_text=True)
        assert '"/card/' in bare, url
        html = client.get(url, headers=PREFIX).get_data(as_text=True)
        assert '"/flashcards/card/' in html, url
        assert '"/card/' not in html, url


def test_static_urls_carry_a_content_hash(client):
    """Caddy caches /static/ for a year; the ?v= hash changes when a file does."""
    html = client.get("/").get_data(as_text=True)
    for name in ("style.css", "base.js"):
        assert f"/static/{name}?v=" in html, name


def test_shared_script_is_a_static_file(client):
    """base.js holds the shared page script; only its URLs stay in the page."""
    html = client.get("/", headers=PREFIX).get_data(as_text=True)
    assert 'src="/flashcards/static/base.js?v=' in html
    assert 'searchData: "/flashcards/search-data.json"' in html
    assert "function openSearch" not in html
    js = client.get("/static/base.js").get_data(as_text=True)
    assert "function openSearch" in js and "FC_URLS.searchData" in js
    assert "{{" not in js


def test_edit_mode_puts_the_csrf_token_in_the_page(client, edit_enabled):
    resp = client.get(CARD)
    with client.session_transaction() as sess:
        token = sess.get("csrf_token")
    assert token and token in resp.get_data(as_text=True)


def test_request_connections_are_read_only(app):
    import sqlite3

    import app.db as db

    with app.test_request_context("/"):
        with pytest.raises(sqlite3.OperationalError, match="readonly"):
            db.get_db().execute("DELETE FROM edges")


def test_edit_mode_connections_can_write(app, edit_enabled):
    import app.db as db

    with app.test_request_context("/"):
        db.get_db().execute("DELETE FROM edges WHERE 0")


def test_templates_are_dedented(client):
    html = client.get("/").get_data(as_text=True)
    assert "\n  <" not in html  # template indentation is stripped
    assert 'class="card-tile"\nhref=' in html  # newlines kept: tokens stay apart
