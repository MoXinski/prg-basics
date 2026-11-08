def f(text):
    result = ''
    for char in text:
        if result == '':
            result = char
        else:
            result = result + '-' + char
    return result

print(f('University'))
print(f('UE'))
print(f('x'))
print(f(''))
