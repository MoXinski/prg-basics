number = int(input('Enter decimal number: '))
n = number
binary = ''

if n == 0:
    binary = '0'

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print(f'{number}(10) = {binary}(2)')
