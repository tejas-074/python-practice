def common_items(first, second):
    return sorted(set(first) & set(second))

print(common_items([1, 2, 3, 4], [3, 4, 5, 6]))
print(common_items(["chrome", "firefox", "edge"], ["edge", "safari", "chrome"]))
print(common_items([1, 2], [3, 4]))
print(common_items([1, 1, 2, 2], [2, 2, 3]))