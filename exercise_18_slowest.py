def get_duration(test):
    return test["duration"]

def slowest_tests(results, count):
    ordered = sorted(results, key=get_duration, reverse=True)
    return ordered[:count]

results = [
    {"name": "login", "duration": 2.5},
    {"name": "search", "duration": 8.1},
    {"name": "cart", "duration": 4.0},
    {"name": "checkout", "duration": 12.3},
    {"name": "logout", "duration": 1.2},
]

for test in slowest_tests(results, 3):
    print(f"{test['name']}: {test['duration']} seconds")