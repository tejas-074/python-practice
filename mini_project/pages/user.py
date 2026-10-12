class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"Typing username: {self.username}")
        print(f"Typing password: {self.password}")
        print("Clicking Login")

    def is_locked(self):
        return self.username == "locked_out_user"