from playwright.sync_api import Page, expect

def test_dynamic_loading(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button", name="start").click()
    expect(page.get_by_text("Hello World!")).to_be_visible(timeout=10000)


def test_enable_textbox(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")
    textbox = page.get_by_role("textbox")
    expect(textbox).to_be_disabled()
    page.get_by_role("button", name="Enable").click()
    expect(textbox).to_be_enabled(timeout=10000)
    textbox.fill("Hello")
    expect(textbox).to_have_value("Hello")