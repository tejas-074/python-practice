from playwright.sync_api import Page, expect

URL = "https://the-internet.herokuapp.com/javascript_alerts"

def test_alert(page: Page):
    page.goto(URL, wait_until="domcontentloaded")
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

def test_confirm_cancel(page: Page):
    page.goto(URL, wait_until="domcontentloaded")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")

def test_prompt(page: Page):
    page.goto(URL, wait_until="domcontentloaded")
    page.once("dialog", lambda dialog: dialog.accept("Tejas"))
    page.get_by_role("button", name="Click for JS Prompt").click()
    expect(page.locator("#result")).to_have_text("You entered: Tejas")