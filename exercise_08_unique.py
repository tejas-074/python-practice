def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)

    return unique

print(remove_duplicates([1, 2, 2, 3, 1]))
print(remove_duplicates(["chrome", "firefox", "chrome", "edge"]))
print(remove_duplicates([5, 5, 5, 5]))