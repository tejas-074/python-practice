from playwright.sync_api import expect

def test_add_backpack(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")