import json
import pytest

def test_formulas_route(client):
    """Verify that the formulas route aggregates formulas by topic."""
    response = client.get('/formulas')
    assert response.status_code == 200
    # Check for some known formulas
    # Formula Sheet subtitle
    assert b'All Key Formula sections, grouped by topic' in response.data
    # A card name that has formulas
    assert b'Black-Scholes Equation' in response.data
    # Some math content from that card
    assert b'C = S_0' in response.data

def test_formulas_route_grouping(client):
    """Check that formulas are grouped into topic sections."""
    response = client.get('/formulas')
    assert response.status_code == 200
    # Topic dots for topics that have formulas
    assert b'topic-dot' in response.data
    # Topic headings for Calculus, Derivatives etc.
    assert b'Calculus' in response.data
    assert b'Derivatives' in response.data
