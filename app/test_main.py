from fastapi.testclient import TestClient
from main import app
from crud import hash_password
import json


client = TestClient(app)


def test_create_user(): 
    data = {
        "first_name": "John", 
        "last_name":"Doe", 
        "email":"johndoe@email.com", 
        "password":"password123"
    }
    response = client.post(
        "/users/", 
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        assert response.status_code == 200
    if response.status_code == 400:
        assert response.status_code == 400
        assert response.json() == {"detail":"ERROR: This Email has already been registered"}

def test_create_user_with_short_password(): 
    data = {
        "first_name": "John", 
        "last_name":"Doe", 
        "email":"johndoe@email.com", 
        "password":"pwd"
    }
    response = client.post(
        "/users/", 
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    assert response.status_code == 400
    assert response.json() == {"detail":"ERROR: Password needs to have a minimum of 8 characters"}

