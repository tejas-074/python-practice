numbers = [1, 2, 3, 4, 5]

squares = []
for n in numbers:
    squares.append(n * n)
print(squares)

squares_short = [n * n for n in numbers]
print(squares_short)

usernames = ["  Standard_User ", "LOCKED_OUT_USER", "Problem_User"]
clean = [name.strip().lower() for name in usernames]
print(clean)

lengths = [len(name) for name in clean]
print(lengths)