def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count

print(count_vowels("Tejas"))
print(count_vowels("automation"))
print(count_vowels("Python"))
print(count_vowels("AEIOU"))
    