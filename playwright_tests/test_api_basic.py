from playwright.sync_api import Playwright

def test_get_post(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    response = api.get("/posts/1")
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    api.dispose()

def test_create_post(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    response = api.post("/posts", data={"title": "my post", "body": "hello", "userId": 1})
    assert response.status == 201
    data = response.json()
    assert data["title"] == "my post"
    api.dispose()