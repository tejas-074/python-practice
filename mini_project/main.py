from utils.helpers import make_email
from pages.user import User

email = make_email("tester")
user = User(email, "secret_sauce")
user.login()