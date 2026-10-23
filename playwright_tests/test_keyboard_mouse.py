from playwright.sync_api import Page, expect

def test_keyboard(page: Page):
    page.goto("https://the-internet.herokuapp.com/key_presses", wait_until="domcontentloaded")
    page.locator("#target").press("A")
    expect(page.locator("#result")).to_have_text("You entered: A")

def test_drag_and_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop", wait_until="domcontentloaded")
    page.locator("#column-a").drag_to(page.locator("#column-b"))
    expect(page.locator("#column-a header")).to_have_text("B")
    expect(page.locator("#column-b header")).to_have_text("A")