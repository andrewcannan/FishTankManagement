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
    assert data['fish_list'] == []
    assert data['fish_types'] == ['Goldfish', 'Angelfish', 'Babelfish']
    assert data['days_until_cleaning'] == 30
    assert data['total_food_required'] == 0.0
    
def test_add_fish(client):
    new_fish_data = {
        'fish_type': 'Goldfish',
        'fish_name': 'Goldie'
    }
    response = client.post('/add_fish', json=new_fish_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Fish added successfully.'
    assert data['tank_status']['total_food_required'] == 0.1
    assert data['tank_status']['days_until_cleaning'] == 29

def test_tank_after_adding_fish(client):
    response = client.get('/tank')
    assert response.status_code == 200
    data = response.get_json()
    assert data['fish_list'][0]['name'] == 'Goldie'
    assert data['fish_list'][0]['food_required'] == 0.1
    assert data['fish_types'] == ['Goldfish', 'Angelfish', 'Babelfish']
    assert data['days_until_cleaning'] == 29
    assert data['total_food_required'] == 0.1
    
def test_add_fish_type(client):
    new_fish_type = {
        'fish_type': 'Clownfish',
        'food_required': 0.4
    }
    response = client.post('/add_fish_type', json=new_fish_type)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'New fish type Clownfish added successfully.'
    
def test_missing_data_add_fish(client):
    new_fish_data = {
        'fish_type': 'Goldfish'
    }
    response = client.post('/add_fish', json=new_fish_data)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type and name are required.'
    new_fish_data_2 = {
        'fish_name': 'Goldie'
    }
    response = client.post('/add_fish', json=new_fish_data_2)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type and name are required.'
    new_fish_data_3 = {}
    response = client.post('/add_fish', json=new_fish_data_3)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type and name are required.'
    
def test_empty_string_add_fish(client):
    new_fish_data = {
        'fish_type': '',
        'fish_name': 'Goldie'
    }
    response = client.post('/add_fish', json=new_fish_data)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type and Name must be provided as a non-empty string.'
    new_fish_data_2 = {
        'fish_type': 'Goldfish',
        'fish_name': ''
    }
    response = client.post('/add_fish', json=new_fish_data_2)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type and Name must be provided as a non-empty string.'
    
def test_missing_data_add_fish_type(client):
    new_fish_type = {
        'fish_type': 'Clownfish'
    }
    response = client.post('/add_fish_type', json=new_fish_type)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type and food amount are required.'
    new_fish_type_2 = {
        'food_required': 0.4
    }
    response = client.post('/add_fish_type', json=new_fish_type_2)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type and food amount are required.'
    
def test_empty_string_add_fish_type(client):
    new_fish_type = {
        'fish_type': '',
        'food_required': 0.4
    }
    response = client.post('/add_fish_type', json=new_fish_type)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type must be provided as a non-empty string.'
    
def test_non_number_add_fish_type(client):
    new_fish_type = {
        'fish_type': 'Clownfish',
        'food_required': 'Apple'
    }
    response = client.post('/add_fish_type', json=new_fish_type)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Food amount must be a valid number. E.g - 0.1'
    
def test_add_duplicate_fish_type(client):
    new_fish_type = {
        'fish_type': 'Goldfish',
        'food_required': 0.1
    }
    response = client.post('/add_fish_type', json=new_fish_type)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type Goldfish already exists.'
    
def test_add_non_existent_fish_type(client):
    new_fish_data = {
        'fish_type': 'Blowfish',
        'fish_name': 'Blowie'
    }
    response = client.post('/add_fish', json=new_fish_data)
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Fish type not found.'