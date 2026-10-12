import random
from datetime import datetime

number = random.randint(1000, 9999)
email = f"user{number}@example.com"
print(email)

browser = random.choice(["chrome", "firefox", "edge"])
print(browser)

today = datetime.now()
print(today.strftime("%Y-%m-%d"))