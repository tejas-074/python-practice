from playwright.sync_api import expect
def test_first_and_second_button(logged_in_page):
    buttons = logged_in_page.get_by_role("button", name="Add to cart")
    buttons.first.click()
    buttons.nth(1).click()
    expect(logged_in_page.get_by_role("button", name="Remove")).to_have_count(2)