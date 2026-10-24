from playwright.sync_api import expect

def test_api_login_then_open_secure_page(playwright, browser):
    api = playwright.request.new_context(base_url="https://the-internet.herokuapp.com")
    response = api.post("/authenticate", form={"username": "tomsmith", "password": "SuperSecretPassword!"})
    assert response.ok
    state = api.storage_state()

    context = browser.new_context(storage_state=state)
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/secure", wait_until="domcontentloaded")
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()

    context.close()
    api.dispose()