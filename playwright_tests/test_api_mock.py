from playwright.sync_api import expect

def test_mock_todo(page):
    def fake_answer(route):
        route.fulfill(status=200, json={"id": 1, "title": "Learn mocking", "completed": True})

    page.route("https://jsonplaceholder.typicode.com/todos/1", fake_answer)
    page.goto("https://jsonplaceholder.typicode.com/todos/1", wait_until="domcontentloaded")
    expect(page.locator("body")).to_contain_text("Learn mocking")

def test_mock_server_error(page):
    def broken_server(route):
        route.fulfill(status=500, body="Server is down")

    page.route("**/todos/1", broken_server)
    response = page.goto("https://jsonplaceholder.typicode.com/todos/1", wait_until="domcontentloaded")
    assert response.status == 500
    expect(page.locator("body")).to_contain_text("Server is down")