from playwright.sync_api import Page, expect

def test_table_cells(page: Page):
    page.goto("https://the-internet.herokuapp.com/tables", wait_until="domcontentloaded")
    rows = page.locator("#table2 tbody tr")

    doe = rows.filter(has_text="Doe")
    expect(doe.locator(".email")).to_have_text("jdoe@hotmail.com")

    bach = rows.filter(has_text="Bach")
    expect(bach.locator(".dues")).to_have_text("$51.00")

    conway = rows.filter(has_text="Conway")
    conway.get_by_role("link", name="delete").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/tables#delete")

def test_dropdown(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown", wait_until="domcontentloaded")
    dropdown = page.get_by_role("combobox")
    dropdown.select_option("Option 2")
    expect(dropdown).to_have_value("2")

def test_checkboxes(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes", wait_until="domcontentloaded")
    first = page.get_by_role("checkbox").first
    second = page.get_by_role("checkbox").nth(1)
    first.check()
    expect(first).to_be_checked()
    second.uncheck()
    expect(second).not_to_be_checked()

def test_number_box(page: Page):
    page.goto("https://the-internet.herokuapp.com/inputs", wait_until="domcontentloaded")
    number = page.get_by_role("spinbutton")
    number.fill("76")
    number.press("ArrowUp")
    expect(number).to_have_value("77")

def test_hover(page: Page):
    page.goto("https://the-internet.herokuapp.com/hovers", wait_until="domcontentloaded")
    figure = page.locator(".figure").first
    figure.hover()
    expect(figure.locator(".figcaption")).to_be_visible()
    expect(figure.get_by_role("heading")).to_have_text("name: user1")

def test_dynamic_buttons(page: Page):
    page.goto("https://the-internet.herokuapp.com/challenging_dom", wait_until="domcontentloaded")
    buttons = page.locator("a.button")
    expect(buttons).to_have_count(3)

    red = page.locator("a.button.alert")
    green = page.locator("a.button.success")
    expect(red).to_have_count(1)
    expect(green).to_have_count(1)

    red.click()
    expect(buttons).to_have_count(3)

def test_nested_frames(page: Page):
    page.goto("https://the-internet.herokuapp.com/nested_frames", wait_until="domcontentloaded")
    top = page.frame_locator('[name="frame-top"]')
    expect(top.frame_locator('[name="frame-left"]').locator("body")).to_contain_text("LEFT")
    expect(top.frame_locator('[name="frame-middle"]').locator("body")).to_contain_text("MIDDLE")
    expect(top.frame_locator('[name="frame-right"]').locator("body")).to_contain_text("RIGHT")
    expect(page.frame_locator('[name="frame-bottom"]').locator("body")).to_contain_text("BOTTOM")