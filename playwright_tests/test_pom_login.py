from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_with_page_object(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    expect(page.get_by_test_id("title")).to_have_text("Products")