def divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")

divide(10, 2)
divide(10, 0)
print("Test continues")