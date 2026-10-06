def get_even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

print(get_even_numbers([1, 2, 3, 4, 5, 6]))
print(get_even_numbers([7, 9, 11]))
print(get_even_numbers([10, 15, 20, 25, 30]))