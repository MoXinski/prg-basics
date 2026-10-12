###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone_number = input('Enter phone number: ')
print(f'{phone_number[0:3]}-{phone_number[3:6]}-{phone_number[6:9]}')