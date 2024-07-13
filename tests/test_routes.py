import pytest
from flask import Flask, jsonify
from app import app, tank

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
def test_current_tank(client):
    response = client.get('/tank')
    assert response.status_code == 200
    data = response.get_json()
    assert 'fish_types' in data
    assert 'fish_list' in data
    assert 'days_until_cleaning' in data
    assert 'total_food_required' in data