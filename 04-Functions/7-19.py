def f(number):
    text = str(number)
    total = 0
    for char in text:
        if text.count(char) > 1:
            total += int(char)
    return total

print(f(1027))
print(f(230335))
print(f(513553007))
