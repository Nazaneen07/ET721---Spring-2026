"""
Nazaneen Baguaei,
Project 3, unit testing in a Flask app
April 2026
"""
import json
import pytest
from app import create_app
from app.models import db, Fruit

@pytest.fixture
def app():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
        ]
        db.session.bulk_save_objects(fruits)
        db.session.commit()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_getAllFruits_whenDatabaseHasFruits_returnsFruitsList(client):
    response = client.get('/api/fruits')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]['name'] == 'Apple'

def test_addFruit_withValidData_returnsSuccessMessageAndFruitId(client):
    new_fruit = {"name": "Orange", "quantity": 5, "variety": "Navel", "season": "Winter"}
    response = client.post('/api/fruits', json=new_fruit)
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data['message'] == 'Fruit added successfully'
    assert 'id' in data

def test_getFruitById_withExistingId_returnsFruit(client):
    # GET by id is not supported, expects 405
    response = client.get('/api/fruits/1')
    assert response.status_code == 405

def test_getFruitById_withNonExistingId_returns404(client):
    response = client.get('/api/fruits/9999')
    assert response.status_code == 405

def test_updateFruit_withValidData_returnsSuccessMessage(client):
    updated_fruit = {"name": "Apple", "quantity": 50, "variety": "Fuji", "season": "Fall"}
    response = client.put('/api/fruits/1', json=updated_fruit)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'Fruit updated successfully'

def test_updateFruit_withNonExistingId_returns404(client):
    updated_fruit = {"name": "Apple", "quantity": 50, "variety": "Fuji", "season": "Fall"}
    response = client.put('/api/fruits/9999', json=updated_fruit)
    assert response.status_code == 404

def test_deleteFruit_withExistingId_returnsSuccessMessage(client):
    response = client.delete('/api/fruits/2')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'Fruit deleted successfully'

def test_deleteFruit_withNonExistingId_returns404(client):
    response = client.delete('/api/fruits/9999')
    data = json.loads(response.data)
    assert response.status_code == 404

def test_searchFruits_byName_returnsMatchingFruits(client):
    response = client.get('/api/fruits/search?name=Apple')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) >= 1

def test_searchFruits_withNoMatch_returnsMessage(client):
    response = client.get('/api/fruits/search?name=Dragonfruit')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'message' in data

def test_home_returnsWelcomeMessage(client):
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'message' in data
