from playwright.sync_api import expect

HTML = "<h1>Shop</h1><button id='buy'>Buy now</button><p id='price'>Price: 499</p>"

def test_heading(page):
    page.set_content(HTML)
    expect(page.get_by_role("heading", name="Shop")).to_be_visible()

def test_button(page):
    page.set_content(HTML)
    expect(page.get_by_role("button", name="Buy now")).to_be_visible()

def test_price(page):
    page.set_content(HTML)
    expect(page.locator("#price")).to_have_text("Price: 499")