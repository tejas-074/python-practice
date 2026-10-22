import pytest
from playwright.sync_api import Page

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


