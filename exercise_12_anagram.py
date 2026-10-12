def is_anagram(first, second):
    a = first.lower().replace(" ", "")
    b = second.lower().replace(" ", "")
    return sorted(a) == sorted(b)

print(is_anagram("listen", "silent"))
print(is_anagram("Dormitory", "dirty room"))
print(is_anagram("hello", "world"))
print(is_anagram("abc", "abcd"))