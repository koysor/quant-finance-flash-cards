"""Test suite for search context and index page filtering."""
import json
import pytest

def test_search_data_json_context(client):
    """Verify pages load search data from /search-data.json and it is valid."""
    response = client.get('/')
    assert response.status_code == 200
    # base.html fetches the card index lazily rather than embedding it.
    assert b"fetch('/search-data.json')" in response.data

    data = client.get('/search-data.json')
    assert data.status_code == 200
    assert data.mimetype == 'application/json'
    cards = data.get_json()
    assert cards
    assert {'id', 'name', 'topic', 'tags', 'url', 'colour'} <= set(cards[0])

def test_index_filtering_tag(client):
    """Verify that the index route correctly filters by tag."""
    # Pick a tag that exists, like 'options'
    response = client.get('/?tag=options')
    assert response.status_code == 200
    # Grouped data should only contain cards with 'options' tag in the visible grid.
    # We check for the card-tile-name span to distinguish from ALL_CARDS JSON.
    assert b'class="card-tile-name">Black-Scholes Equation</span>' in response.data
    # 'Taylor Series' (Calculus) should NOT be in the visible grid when filtered by 'options'
    assert b'class="card-tile-name">Taylor Series</span>' not in response.data

def test_index_filtering_topic(client):
    """Verify that the index route correctly filters by topic."""
    response = client.get('/?topic=Calculus')
    assert response.status_code == 200
    assert b'class="card-tile-name">Taylor Series</span>' in response.data
    assert b'class="card-tile-name">Black-Scholes Equation</span>' not in response.data
