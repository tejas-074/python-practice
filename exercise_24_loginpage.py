class LoginPage:
    def __init__(self, url):
        self.url = url
        self.logged_in = False
        self.attempts = 0

    def login(self, username, password):
        self.attempts += 1
        if username == "locked_out_user":
            raise ValueError("User is locked out")
        if password != "secret_sauce":
            raise ValueError("Wrong password")
        self.logged_in = True

page = LoginPage("https://www.saucedemo.com")

users = [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "wrong"),
]

for username, password in users:
    try:
        page.login(username, password)
        print(f"{username}: logged in")
    except ValueError as error:
        print(f"{username}: {error}")

print(page.attempts)
print(page.logged_in)