import json
from login_page import LoginPage

def load_users(path):
    with open(path) as file:
        return json.load(file)

def run_login_test(user):
    page = LoginPage("https://www.saucedemo.com")
    try:
        page.login(user["username"], user["password"])
        actual = "success"
    except ValueError:
        actual = "locked"
    return actual

users = load_users("users.json")
passed = 0

for user in users:
    actual = run_login_test(user)
    if user["expected"] == actual:
        print(f"{user['username']}: PASS")
        passed += 1
    else:
        print(f"{user['username']}: FAIL (expected {user['expected']}, got {actual})")

print(f"Passed {passed} of {len(users)}")