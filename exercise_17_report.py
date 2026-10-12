def save_report(path, results):
    with open(path, "w") as file:
        for test in results:
            file.write(f"{test['name']}: {test['status']}\n")

results = [
    {"name": "login", "status": "pass"},
    {"name": "logout", "status": "pass"},
    {"name": "search", "status": "fail"},
]

save_report("report.txt", results)

with open("report.txt") as file:
    print(file.read())