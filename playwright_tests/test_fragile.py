from playwright.sync_api import expect

def test_sturdy_locator(logged_in_page):
    page = logged_in_page
    page.get_by_test_id("product-sort-container").select_option("lohi")

    item = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    item.get_by_role("button", name="Add to cart").click()
    expect(item.get_by_role("button", name="Remove")).to_be_visible()