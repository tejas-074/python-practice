numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)

results = [
    {"name": "login", "status": "pass"},
    {"name": "logout", "status": "pass"},
    {"name": "search", "status": "fail"},
    {"name": "cart", "status": "pass"},
    {"name": "checkout", "status": "fail"},
]

passed_names = [test["name"] for test in results if test["status"] == "pass"]
print(passed_names)

usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]
long_names = [name for name in usernames if len(name) > 13]
print(long_names)