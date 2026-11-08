def f(expression):
    result = int(expression[0])
    for i in range(1, len(expression), 2):
        if expression[i] == '+':
            result += int(expression[i + 1])
        else:
            result -= int(expression[i + 1])
    return result

print(f('2+3'))
print(f('3+8+1'))
print(f('2+3-4+5-0'))
