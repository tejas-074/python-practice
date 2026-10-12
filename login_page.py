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