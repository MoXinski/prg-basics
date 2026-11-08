def f(product_code):
    total = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    if total % 7 == int(product_code[3]):
        return True
    else:
        return False

print(f('1082'))
print(f('2035'))
print(f('1114'))
print(f('7071'))
