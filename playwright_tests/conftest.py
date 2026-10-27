import pytest
import config
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def logged_in_page(page: Page) -> Page:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    return page

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page, login_page):
    login_page.open()
    login_page.login(config.USERNAME, config.PASSWORD)
    return InventoryPage(page)

@pytest.fixture
def api_logged_in_page(playwright, browser):
    api = playwright.request.new_context(base_url="https://the-internet.herokuapp.com")
    api.post("/authenticate", form={"username": "tomsmith", "password": "SuperSecretPassword!"})
    context = browser.new_context(storage_state=api.storage_state())
    page = context.new_page()
    yield page
    context.close()
    api.dispose()

import base64
from pytest_html import extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            png = base64.b64encode(page.screenshot()).decode()
            report.extras = getattr(report, "extras", []) + [extras.png(png)]