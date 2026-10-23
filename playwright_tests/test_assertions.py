from playwright.sync_api import expect

def test_assertion_tour(logged_in_page):
    page = logged_in_page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_title("Swag Labs")
    expect(page.locator(".inventory_item")).to_have_count(6)

    backpack_button = page.get_by_test_id("add-to-cart-sauce-labs-backpack")
    expect(backpack_button).to_have_attribute("id", "add-to-cart-sauce-labs-backpack")

    badge = page.locator(".shopping_cart_badge")
    expect(badge).to_have_count(0)

    backpack_button.click()
    expect(badge).to_have_text("1")
    expect(backpack_button).not_to_be_visible()