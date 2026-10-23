import re
from playwright.sync_api import Page, expect

def test_fill_and_submit_form(page: Page):
    page.goto("https://www.selenium.dev/selenium/web/web-form.html", wait_until="domcontentloaded")
    page.get_by_label("Text input").fill("Tejas")
    page.get_by_label("Password").fill("secret")
    page.get_by_label("Textarea").fill("Learning Playwright")

    radio = page.get_by_role("radio", name="Default radio")
    radio.check()
    expect(radio).to_be_checked()

    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("heading")).to_have_text("Form submitted")

def test_upload_and_dropdown(page: Page, tmp_path):
    sample = tmp_path / "report.txt"
    sample.write_text("test data")

    page.goto("https://www.selenium.dev/selenium/web/web-form.html", wait_until="domcontentloaded")
    page.get_by_label("File input").set_input_files(str(sample))

    dropdown = page.get_by_label("Dropdown (select)")
    dropdown.select_option(label="Two")
    expect(dropdown).to_have_value("2")

    page.get_by_role("button", name="Submit").click()
    expect(page).to_have_url(re.compile("report.txt"))