def mask(text):
    if len(text) <= 4:
        return text
    hidden = "*" * len(text[:-4])
    return hidden + text[-4:]

print(mask("9876543210"))
print(mask("123456789"))
print(mask("abc"))
print(mask("tejas"))