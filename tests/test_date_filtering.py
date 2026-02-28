"""Test suite for date range filtering and API responses."""
import json
import pytest

def test_recent_route_json_response(client):
    """Test that /recent returns JSON when requested."""
    response = client.get('/recent', headers={'Accept': 'application/json'})
    assert response.status_code == 200
    # response.is_json might not be reliable if charset is included, check content_type
    assert 'application/json' in response.content_type
    data = response.get_json()
    assert isinstance(data, list)
    if data:
        # Check basic fields
        assert 'id' in data[0]
        assert 'name' in data[0]
        assert 'created_date' in data[0]

def test_recent_route_filtering_by_date(client):
    """Test that /recent correctly filters by date."""
    # First get all cards to see what we have
    full_response = client.get('/recent?format=json')
    all_data = full_response.get_json()
    
    if not all_data:
        pytest.skip("No cards in database to test filtering.")

    # Find unique dates and pick a range
    dates = sorted(list({c['created_date'] for c in all_data if c['created_date']}))
    if len(dates) < 2:
        # If we only have one date, we can still test equality filtering
        start_date = dates[0]
        end_date = dates[0]
    else:
        start_date = dates[0]
        end_date = dates[-1]

    start_date_param = start_date
    end_date_param = end_date
    if len(start_date_param) == 10:
        start_date_param = f"{start_date_param} 00:00:00"
    if len(end_date_param) == 10:
        end_date_param = f"{end_date_param} 23:59:59"

    # Filter with start and end
    filtered_response = client.get(f'/recent?format=json&start={start_date_param}&end={end_date_param}')
    filtered_data = filtered_response.get_json()
    
    # Check that all returned cards are within range
    for card in filtered_data:
        assert start_date_param <= card['created_date'] <= end_date_param

def test_recent_route_default_sorting(client):
    """Test that /recent defaults to newest record (DESC order)."""
    response = client.get('/recent?format=json')
    data = response.get_json()
    
    if len(data) < 2:
        pytest.skip("Not enough cards to test sorting.")

    # Dates should be in descending order
    dates = [c['created_date'] for c in data if c['created_date']]
    assert dates == sorted(dates, reverse=True)

def test_recent_route_invalid_dates(client):
    """Test that invalid date formats don't crash the app."""
    response = client.get('/recent?start=not-a-date&end=xyz')
    assert response.status_code == 200
