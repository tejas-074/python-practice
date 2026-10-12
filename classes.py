class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def describe(self):
        print(f"User {self.username} is ready to log in")

user1 = User("standard_user", "secret_sauce")
user2 = User("problem_user", "secret_sauce")

print(user1.username)
user1.describe()
user2.describe()