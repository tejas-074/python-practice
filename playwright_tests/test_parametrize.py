import pytest
from playwright.sync_api import Page, expect

@pytest.mark.regression
@pytest.mark.parametrize("username, password, expected", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out"),
    ("standard_user", "wrong", "Epic sadface: Username and password do not match any user in this service"),
    ("", "", "Epic sadface: Username is required"),
])
def test_login_errors(page: Page, username, password, expected):
    page.goto("https://www.saucedemo.com")
    page.get_by_test_id("username").fill(username)
    page.get_by_test_id("password").fill(password)
    page.get_by_test_id("login-button").click()
    expect(page.get_by_test_id("error")).to_contain_text(expected)