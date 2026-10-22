from playwright.sync_api import expect

def test_add_backpack_by_name(logged_in_page):
    item = logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    item.get_by_role("button", name="Add to cart").click()
    expect(item.get_by_role("button", name="Remove")).to_be_visible()