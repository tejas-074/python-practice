def group_by_status(results):
    groups = {}
    for test in results:
        status = test["status"]
        if status not in groups:
            groups[status] = []
        groups[status].append(test["name"])
    return groups

results = [
    {"name": "login", "status": "pass"},
    {"name": "logout", "status": "pass"},
    {"name": "search", "status": "fail"},
    {"name": "cart", "status": "pass"},
    {"name": "checkout", "status": "fail"},
]

print(group_by_status(results))
print(group_by_status([]))