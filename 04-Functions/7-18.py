def f(sentence):
    result = ''
    for char in sentence:
        if char != ' ':
            result = result + char
    return result

print(f('integrated development environment'))
print(f('A programming language is a system of notation for writing computer programs'))
