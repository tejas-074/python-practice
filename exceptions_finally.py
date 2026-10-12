def run_test(name, should_fail):
    print(f"Starting {name}")
    try:
        if should_fail:
            raise Exception("Element not found")
        print(f"{name} passed")
    except Exception as error:
        print(f"{name} failed: {error}")
    finally:
        print(f"Closing browser for {name}")

run_test("login test", False)
run_test("search test", True)