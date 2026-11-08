def f(n):
    text = '*'
    for i in range(n - 1):
        text = text + '/*'
    return text

print(f(4))
print(f(1))
