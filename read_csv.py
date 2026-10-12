import csv

with open("users.csv", newline="") as file:
    reader = csv.DictReader(file)
    users = list(reader)

print(len(users))
print(users[0])

for user in users:
    print(f"{user['username']} -> {user['expected']}")

success_users = [u["username"] for u in users if u["expected"] == "success"]
print(success_users)