from user import User

user1 = User("standard_user", "secret_sauce")
user2 = User("locked_out_user", "secret_sauce")

user1.login()
print(user2.is_locked())