import pytest

@pytest.fixture
def api(playwright):
    context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    yield context
    context.dispose()

def test_create_post(api):
    response = api.post("/posts", data={"title": "QA", "body": "learning", "userId": 1})
    assert response.status == 201
    assert response.json()["title"] == "QA"

def test_update_post(api):
    response = api.put("/posts/1", data={"id": 1, "title": "new", "body": "x", "userId": 1})
    assert response.status == 200
    assert response.json()["title"] == "new"

def test_delete_post(api):
    response = api.delete("/posts/1")
    assert response.status == 200