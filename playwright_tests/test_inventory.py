from playwright.sync_api import expect

def test_six_products(logged_in_page):
    expect(logged_in_page.locator('.inventory_item')).to_have_count(6)