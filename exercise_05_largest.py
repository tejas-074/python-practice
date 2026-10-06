def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(find_largest([3, 9, 2, 7]))
print(find_largest([10, 5, 8]))
print(find_largest([-5, -2, -9]))