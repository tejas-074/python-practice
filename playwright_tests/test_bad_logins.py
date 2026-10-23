import json
from pathlib import Path
import pytest
from playwright.sync_api import expect

DATA = Path(__file__).parent / "test_data" / "bad_logins.json"
with open(DATA) as f:
    CASES = json.load(f)

@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_bad_login(login_page, case):
    login_page.open()
    login_page.login(case["username"], case["password"])
    expect(login_page.error).to_contain_text(case["message"])