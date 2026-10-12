import json

with open("users.json") as file:
    users = json.load(file)

print(len(users))
print(users[0]["username"])

for user in users:
    print(f"{user['username']} -> {user['expected']}")