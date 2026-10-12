tests = ["login", "logout", "search"]
statuses = ["pass", "pass", "fail"]

for number, test in enumerate(tests, start=1):
    print(f"{number}. {test}")

for test, status in zip(tests, statuses):
    print(f"{test}: {status}")

failed = [t for t, s in zip(tests, statuses) if s == "fail"]
print(failed)