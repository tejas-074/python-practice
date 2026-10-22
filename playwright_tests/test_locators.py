from playwright.sync_api import Page, expect

def test_login_with_user_facing_locators(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products", exact=True)).to_be_visible()

def test_login_with_test_ids(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_test_id("username").fill("standard_user")
    page.get_by_test_id("password").fill("secret_sauce")
    page.get_by_test_id("login-button").click()
    expect(page.get_by_test_id("title")).to_have_text("Products")