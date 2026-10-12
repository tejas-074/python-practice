import random

def make_email(prefix="user"):
    number = random.randint(1000, 9999)
    return f"{prefix}{number}@example.com"

def clean_username(name):
    return name.strip().lower()