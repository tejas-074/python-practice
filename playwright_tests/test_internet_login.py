from playwright.sync_api import Page, expect

def test_internet_login_success(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

def test_internet_login_wrong_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("wrongpassword")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")