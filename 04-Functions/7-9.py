def f(number, even):
    total = 0
    for char in str(number):
        digit = int(char)
        if even and digit % 2 == 0:
            total += digit
        elif not even and digit % 2 == 1:
            total += digit
    return total

print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))
