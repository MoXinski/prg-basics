import number_range

number = int(input('A number: '))

if number_range.in_range(number, 2, 15):
    print(f'Number {number} in the range <2,15>: yes')
else:
    print(f'Number {number} in the range <2,15>: no')
