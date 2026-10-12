def get_error_lines(path):
    errors = []
    with open(path) as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line.strip())
    return errors

errors = get_error_lines("test_log.txt")
print(len(errors))
for error in errors:
    print(error)