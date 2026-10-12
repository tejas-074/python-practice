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

user1 = User("standard_user", "secret_sauce")
user2 = User("locked_out_user", "secret_sauce")

user1.login()
print(user1.is_locked())
print(user2.is_locked())