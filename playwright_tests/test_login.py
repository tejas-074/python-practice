from playwright.sync_api import expect
import config

def test_login_success(login_page):
    login_page.open()
    login_page.login(config.USERNAME, config.PASSWORD)
    expect(login_page.page.get_by_test_id("title")).to_have_text("Products")