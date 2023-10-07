import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index(client):
    response = client.get('/')
    assert b'Todo List' in response.data

def test_add_task(client):
    response = client.post('/add', data={'task': 'Test Task'})
    assert response.status_code == 302
    response = client.get(response.headers['Location'])
    assert b'Test Task' in response.data 

def test_complete_task(client):
    response = client.get('/complete/1')
    assert response.status_code == 302  # Redirect status code

