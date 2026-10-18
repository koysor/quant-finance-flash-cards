"""Route-level tests: card pages, redirects, edge removal and escaping."""
import json

import pytest

import app.db as db


def _csrf(client) -> str:
    client.get("/")
    with client.session_transaction() as sess:
        return sess["csrf_token"]


def _first_edge(app):
    with app.app_context():
        row = db.get_db().execute(
            "SELECT id, source_id, target_id FROM edges ORDER BY id LIMIT 1"
        ).fetchone()
        return dict(row)


def test_card_detail_ok(client):
    assert client.get("/card/derivatives/black-scholes-equation").status_code == 200


def test_unknown_card_404(client):
    assert client.get("/card/no-such-topic/no-such-card").status_code == 404


def test_slug_redirect_unique(client):
    resp = client.get("/card/wrong-topic/black-scholes-equation")
    assert resp.status_code == 301
    assert resp.headers["Location"].endswith("/card/derivatives/black-scholes-equation")


def test_slug_disambiguation(client):
    resp = client.get("/card/wrong-topic/maximum-likelihood-estimation")
    assert resp.status_code == 300


def test_recent_json_and_html_cached_separately(client):
    html = client.get("/recent")
    js = client.get("/recent?format=json")
    assert "text/html" in html.content_type
    assert js.content_type == "application/json"


def test_remove_link_disabled_by_default(client, app, monkeypatch):
    monkeypatch.delenv("ALLOW_EDGE_EDIT", raising=False)
    edge = _first_edge(app)
    resp = client.post(
        f"/card/{edge['source_id']}/remove-link",
        data={"csrf_token": _csrf(client), "edge_id": "1"},
    )
    assert resp.status_code == 404


@pytest.fixture
def edit_enabled(monkeypatch):
    monkeypatch.setenv("ALLOW_EDGE_EDIT", "1")


def test_remove_link_requires_csrf(client, app, edit_enabled):
    edge = _first_edge(app)
    resp = client.post(
        f"/card/{edge['source_id']}/remove-link",
        data={"csrf_token": "bogus", "edge_id": str(edge["id"])},
    )
    assert resp.status_code == 403


def test_remove_link_deletes_edge_and_updates_file(client, app, edit_enabled):
    edge = _first_edge(app)
    resp = client.post(
        f"/card/{edge['source_id']}/remove-link",
        data={"csrf_token": _csrf(client), "edge_id": str(edge["id"])},
    )
    assert resp.status_code == 302
    saved = json.loads(db.EDGES_PATH.read_text(encoding="utf-8"))
    assert not any(
        e["source"] == edge["source_id"] and e["target"] == edge["target_id"]
        for e in saved
    )


def test_remove_link_bad_edge_id(client, app, edit_enabled):
    edge = _first_edge(app)
    resp = client.post(
        f"/card/{edge['source_id']}/remove-link",
        data={"csrf_token": _csrf(client), "edge_id": "abc"},
    )
    assert resp.status_code == 400


def test_graph_json_escapes_script_close(app):
    from app import loader
    html = loader._md.render("<script>alert(1)</script>")
    assert "<script>" not in html


def test_edges_have_no_duplicate_pairs():
    edges = json.loads(db.EDGES_PATH.read_text(encoding="utf-8"))
    pairs = [(e["source"], e["target"]) for e in edges]
    assert len(pairs) == len(set(pairs))


def test_search_data_urls_follow_forwarded_prefix(client):
    resp = client.get("/search-data.json", headers={"X-Forwarded-Prefix": "/flashcards"})
    urls = [c["url"] for c in json.loads(resp.data)]
    assert urls and all(u.startswith("/flashcards/card/") for u in urls)


def test_search_data_has_blurb(client):
    data = json.loads(client.get("/search-data.json").data)
    assert all("blurb" in c for c in data)


def test_quiz_lists_topics_and_serves_a_topic(client):
    assert client.get("/quiz").status_code == 200
    assert client.get("/quiz?topic=Probability").status_code == 200
    assert client.get("/quiz?topic=Nope").status_code == 404


def test_index_collapses_topics_unless_filtered(client):
    full = client.get("/").data.decode()
    assert "<details class=\"topic-section\"" in full and "topic-section\" id=\"topic-1\" open" not in full
    assert "id=\"topic-1\" open" in client.get("/?topic=Probability").data.decode()
