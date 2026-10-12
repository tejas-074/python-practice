import json

def load_users(path):
    with open(path) as file:
        return json.load(file)

def fake_login(username, password):
    if username == "locked_out_user":
        return "locked"
    return "success"

users = load_users("users.json")

for user in users:
    actual = fake_login(user["username"], user["password"])
    if actual == user["expected"]:
        print(f"PASS: {user['username']}")
    else:
        print(f"FAIL: {user['username']} expected {user['expected']} but got {actual}")