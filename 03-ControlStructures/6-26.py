pin = '0805'
attempts = 0
correct = False

while attempts < 3:
    entered_pin = input('Enter the PIN code: ')
    if entered_pin == pin:
        correct = True
        break
    print('Incorrect...')
    attempts += 1

if correct:
    print('PIN code is correct')
else:
    print('Sorry, your payment card has been blocked.')
