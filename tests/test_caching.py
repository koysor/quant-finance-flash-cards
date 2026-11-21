"""Page caching: in-app cache keys, HTTP caching headers and static versioning."""

import pytest

from app.extensions import cache

CARD = "/card/derivatives/black-scholes-equation"
PREFIX = {"X-Forwarded-Prefix": "/flashcards"}


def _page_keys(app) -> list[str]:
    with app.app_context():
        return [k for k in cache.cache._cache if k.startswith("page:")]


@pytest.fixture(autouse=True)
def _no_edit(monkeypatch):
    monkeypatch.delenv("ALLOW_EDGE_EDIT", raising=False)


@pytest.fixture
def edit_enabled(monkeypatch):
    monkeypatch.setenv("ALLOW_EDGE_EDIT", "1")


def test_pages_are_publicly_cacheable_without_cookie(client):
    for url in ("/", CARD, "/quiz", "/graph", "/recent"):
        resp = client.get(url)
        assert resp.status_code == 200, url
        assert resp.headers["Cache-Control"] == "public, max-age=300", url
        assert resp.headers["ETag"].startswith('W/"'), url
        assert "Set-Cookie" not in resp.headers, url
        assert "Cookie" not in resp.headers.get("Vary", ""), url


def test_etag_revalidation_returns_304(client):
    etag = client.get(CARD).headers["ETag"]
    resp = client.get(CARD, headers={"If-None-Match": etag})
    assert resp.status_code == 304
    assert resp.data == b""


def test_search_data_keeps_its_own_max_age(client):
    resp = client.get("/search-data.json")
    assert resp.headers["Cache-Control"] == "public, max-age=86400"
    assert "ETag" in resp.headers


def test_errors_and_redirects_not_publicly_cached(client):
    assert "Cache-Control" not in client.get("/card/no-such/card").headers
    assert "Cache-Control" not in client.get("/random").headers


def test_recent_varies_on_accept(client):
    for url in ("/recent", "/recent?format=json"):
        assert "Accept" in client.get(url).headers.get("Vary", ""), url


def test_unprefixed_request_does_not_poison_prefixed_pages(client):
    # A local request hits / without X-Forwarded-Prefix; the static build sends it.
    # Card links appear as href="..." in pages and as "url": "..." in /graph's JSON.
    for url in ("/", CARD, "/graph"):
        bare = client.get(url).get_data(as_text=True)
        assert '"/card/' in bare, url
        html = client.get(url, headers=PREFIX).get_data(as_text=True)
        assert '"/flashcards/card/' in html, url
        assert '"/card/' not in html, url


def test_only_200_responses_are_cached(client, app):
    client.get("/card/x/junk")  # 404
    client.get("/tag/no-such-tag-anywhere")  # 404
    client.get("/quiz?topic=junk")  # 404
    client.get("/card/wrong-topic/black-scholes-equation")  # 301
    assert _page_keys(app) == []


def test_junk_query_params_share_one_index_entry(client, app):
    client.get("/")
    client.get("/?junk=1")
    client.get("/?junk=2&tag=")
    assert len(_page_keys(app)) == 1


def test_unbounded_inputs_are_not_cached(client, app):
    client.get("/?tag=options")  # thousands of tags, ~400 KB each
    client.get("/?topic=not-a-topic")
    client.get("/recent?start=2026-01-01")  # any date range is valid
    assert _page_keys(app) == []
    client.get("/?topic=Derivatives")
    assert len(_page_keys(app)) == 1


def test_edit_mode_bypasses_page_cache(client, app, edit_enabled):
    for _ in range(2):
        resp = client.get(CARD)
        assert "Cache-Control" not in resp.headers
    assert _page_keys(app) == []
    with client.session_transaction() as sess:
        token = sess.get("csrf_token")
    assert token and token in resp.get_data(as_text=True)


def test_static_urls_are_versioned_and_long_lived(client):
    html = client.get("/").get_data(as_text=True)
    assert "/static/style.css?v=" in html
    href = html.split("/static/style.css?v=", 1)[1].split('"', 1)[0]
    resp = client.get(f"/static/style.css?v={href}")
    assert resp.headers["Cache-Control"] == "public, max-age=31536000, immutable"
    # Unversioned requests keep Flask's revalidating default.
    assert "immutable" not in client.get("/static/style.css").headers.get(
        "Cache-Control", ""
    )


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


def test_cache_threshold_is_configurable(app, monkeypatch):
    from app import create_app

    monkeypatch.setenv("CACHE_THRESHOLD", "7")
    small = create_app()
    with small.app_context():
        assert cache.cache._threshold == 7
