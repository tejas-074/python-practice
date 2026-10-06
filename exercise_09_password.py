def is_valid_password(password):
    if len(password) < 8:
        return False
    for character in password:
        if character.isdigit():
            return True
    return False

print(is_valid_password("abc123"))
print(is_valid_password("abcdefgh"))
print(is_valid_password("automation2026"))
print(is_valid_password("Tejas@123"))