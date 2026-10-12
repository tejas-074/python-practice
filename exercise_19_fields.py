def find_missing_keys(data, required):
    return [key for key in required if key not in data]

def is_valid(data, required):
    missing = find_missing_keys(data, required)
    return len(missing) == 0

response = {"id": 1, "name": "Tejas", "email": "tejas@example.com"}
required = ["id", "name", "email", "phone"]

print(find_missing_keys(response, required))
print(is_valid(response, ["id", "name"]))
print(is_valid(response, required))
print(find_missing_keys({}, ["id"]))