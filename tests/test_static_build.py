"""Static site build (``app/static_site.py``) and the path routes it relies on.

The full build (every page plus the link check) takes about a minute and needs a
Linux file system (the ``P(A|B)`` tag), so CI runs it as its own step; these tests
build a representative subset.
"""

import gzip
import json
from pathlib import PurePosixPath

import pytest
from compression import zstd

import app.db as db
from app.routes import TOPIC_BY_SLUG, topic_slug
from app.static_site import (
    MARKER,
    BuildError,
    build,
    find_missing_links,
    page_urls,
    url_to_file,
)

PREFIX = "/flashcards"


@pytest.fixture
def card_id(app):
    with app.app_context():
        return db.get_all_cards()[0]["id"]


@pytest.fixture
def built(app, tmp_path, card_id):
    urls = [
        "/",
        f"/card/{card_id}",
        "/tag/30/360",
        "/topic/derivatives",
        "/quiz",
        "/quiz/probability",
        "/recent",
        "/random",
        "/barbie",
        "/search-data.json",
    ]
    out = tmp_path / "dist"
    result = build(app, out, PREFIX, urls=urls)
    return out, result


def test_topic_slug_round_trips():
    assert topic_slug("Portfolio Theory & Asset Pricing") == (
        "portfolio-theory-asset-pricing"
    )
    assert len(TOPIC_BY_SLUG) == len(set(TOPIC_BY_SLUG))
    assert TOPIC_BY_SLUG["derivatives"] == "Derivatives"


@pytest.mark.parametrize(
    "url, expected",
    [
        ("/", "index.html"),
        ("/graph", "graph.html"),
        ("/search-data.json", "search-data.json"),
        (
            "/card/derivatives/black-scholes-equation",
            "card/derivatives/black-scholes-equation.html",
        ),
        ("/tag/P%26L%20attribution", "tag/P&L attribution.html"),
        ("/tag/30/360", "tag/30/360.html"),
    ],
)
def test_url_to_file(url, expected):
    assert url_to_file(url) == PurePosixPath(expected)


@pytest.mark.parametrize("url", ["/tag/..", "/tag/a//b", "/tag/%00x"])
def test_url_to_file_rejects_unsafe_names(url):
    with pytest.raises(BuildError):
        url_to_file(url)


def test_page_urls_cover_every_card_tag_and_topic(app):
    urls = page_urls(app)
    with app.app_context():
        cards = db.get_all_cards()
    assert len(urls) == len(set(urls))
    for c in cards[:: max(1, len(cards) // 20)]:
        assert f"/card/{c['id']}" in urls
        assert f"/path/{c['id']}" in urls
    assert "/tag/30/360" in urls
    assert "/topic/portfolio-theory-asset-pricing" in urls
    assert "/quiz/probability" in urls
    for fixed in ("/", "/graph", "/formulas", "/recent", "/quiz", "/random"):
        assert fixed in urls


def test_build_writes_prefixed_pages(built, card_id):
    out, result = built
    assert result.pages == 10
    assert (out / MARKER).is_file()
    index = (out / "index.html").read_text(encoding="utf-8")
    assert f'href="{PREFIX}/card/' in index
    assert f'href="{PREFIX}/static/style.css?v=' in index
    card = (out / f"card/{card_id}.html").read_text(encoding="utf-8")
    assert f'href="{PREFIX}/topic/' in card  # breadcrumb uses the path route
    assert (out / "tag/30/360.html").is_file()
    assert (out / "static/style.css").is_file()
    assert json.loads((out / "recent.json").read_text(encoding="utf-8"))
    assert json.loads((out / "search-data.json").read_text(encoding="utf-8"))


def test_build_writes_browser_stand_ins(built):
    out, _ = built
    assert "goRandom()" in (out / "random.html").read_text(encoding="utf-8")
    assert "theme=barbie" in (out / "barbie.html").read_text(encoding="utf-8")
    not_found = (out / "404.html").read_text(encoding="utf-8")
    assert "slug-matches" in not_found and "Card not found" in not_found
    # Old ?tag= / ?topic= links are forwarded to the path pages.
    index = (out / "index.html").read_text(encoding="utf-8")
    assert "URLSearchParams" in index and f"{PREFIX}/topic/derivatives" in index
    quiz = (out / "quiz.html").read_text(encoding="utf-8")
    assert f"{PREFIX}/quiz/probability" in quiz
    assert "data-date=" in (out / "recent.html").read_text(encoding="utf-8")


def test_build_precompresses_only_large_files(built, card_id):
    out, _ = built
    index = (out / "index.html").read_bytes()
    assert gzip.decompress((out / "index.html.gz").read_bytes()) == index
    assert zstd.decompress((out / "index.html.zst").read_bytes()) == index
    assert not (out / f"card/{card_id}.html.gz").exists()


def test_build_leaves_the_live_app_unchanged(app, built, client):
    """The static stand-ins and their cached pages must not leak into the app."""
    assert not app.config["STATIC_BUILD"]
    assert client.get("/random").status_code == 302
    assert "URLSearchParams" not in client.get("/").data.decode()


def test_missing_links_are_reported(built, card_id):
    out, _ = built
    missing = find_missing_links(out, PREFIX)
    assert f"{PREFIX}/graph" in missing  # linked from the nav, not built here
    assert f"{PREFIX}/card/{card_id}" not in missing
    assert f"{PREFIX}/tag/30/360" not in missing
    assert f"{PREFIX}/" not in missing


def test_build_fails_on_a_non_200_page(app, tmp_path):
    with pytest.raises(BuildError, match="404"):
        build(app, tmp_path / "dist", PREFIX, urls=["/card/no/such-card-anywhere"])


def test_build_refuses_a_foreign_directory(app, tmp_path):
    (tmp_path / "keep.txt").write_text("not a build")
    with pytest.raises(BuildError, match="not a previous build"):
        build(app, tmp_path, PREFIX, urls=["/"])
    assert (tmp_path / "keep.txt").exists()


def test_topic_and_quiz_path_routes(client):
    page = client.get("/topic/derivatives")
    assert page.status_code == 200
    assert 'id="topic-1" open' in page.data.decode()
    assert client.get("/topic/not-a-topic").status_code == 404
    assert client.get("/quiz/probability").status_code == 200
    assert client.get("/quiz/not-a-topic").status_code == 404
    assert 'href="/quiz/probability"' in client.get("/quiz").data.decode()


def test_tag_with_a_slash_has_a_page(client):
    assert client.get("/tag/30/360").status_code == 200
