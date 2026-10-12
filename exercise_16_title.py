def format_test_name(name):
    words = name.split("_")
    return " ".join(word.capitalize() for word in words)

print(format_test_name("login_with_valid_user"))
print(format_test_name("search_returns_no_results"))
print(format_test_name("logout"))