import requests

BASE = "https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(f"{BASE}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "Bret"

def test_create_post():
    payload = {"title": "My post", "body": "Hello", "userId": 1}
    response = requests.post(f"{BASE}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "My post"
    assert "id" in data