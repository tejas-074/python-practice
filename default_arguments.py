def login(username, password="secret_sauce", browser="chrome"):
    print(f"Logging in {username} with password {password} on {browser}")

login("standard_user")
login("problem_user", browser="firefox")
login(password="wrong_pass", username="locked_out_user")