def login(username, password):
    print(f"Typing username: {username}")
    print(f"Typing password: {password}")
    print("Clicking Login")

def add(a, b):
    return a + b

login("standard_user", "secret_sauce")
login("locked_out_user", "secret_sauce")

total = add(10, 5)
print(total)