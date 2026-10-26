def is_binary(number):
    amount = len(number)
    if number.count('0') + number.count('1') == amount:
        return True
    else:
        return False

number = input("Enter a number: ")
if is_binary(number) == True:
    print("This is a binary number.")
else:
    print('This is not a binary number.')