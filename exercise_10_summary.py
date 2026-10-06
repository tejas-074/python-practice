def summarized(results):
    passed = 0
    failed = 0
    for test in results:
        if test['status'] == 'pass':
            passed += 1
        else:
            failed += 1

    return passed, failed

results = [
    {"name": "login", "status": "pass"},
    {"name": "logout", "status": "pass"},
    {"name": "search", "status": "fail"},
    {"name": "cart", "status": "pass"},
    {"name": "checkout", "status": "fail"},
]

passed, failed = summarized(results)
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total: {len(results)}")