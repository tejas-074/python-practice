user = {"username": "standard_user", "password": "secret_sauce"}

print(user)
print(user["username"])
print(user["password"])

user["role"] = "tester"
print(user)

user["password"] = "new_password"
print(user["password"])