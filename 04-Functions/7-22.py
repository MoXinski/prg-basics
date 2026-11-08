def f(name):
    result = ''
    for word in name.split():
        result = result + word[0]
    return result

print(f('Internet of Things'))
print(f('For Your Information'))
print(f('Python'))
