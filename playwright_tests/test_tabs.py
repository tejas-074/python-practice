from playwright.sync_api import Page, expect

def test_new_tab(page: Page):
    page.goto("https://the-internet.herokuapp.com/windows", wait_until="domcontentloaded")

    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Click Here").click()
    new_page = popup_info.value
    new_page.wait_for_load_state()

    expect(new_page).to_have_url("https://the-internet.herokuapp.com/windows/new")
    expect(new_page.get_by_role("heading")).to_have_text("New Window")
    expect(page.get_by_role("heading", name="Opening a new window")).to_be_visible()