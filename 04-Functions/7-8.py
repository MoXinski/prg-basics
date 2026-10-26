def minimum_coin_number(amount):
    if amount % 5 == 0:
        coin_amount = amount//5
    elif amount % 5 == 1:
        coin_amount = (amount//5)+1
    elif amount % 5 == 2:
        coin_amount = (amount//5)+1
    elif amount % 5 == 3:
        coin_amount = (amount//5)+2
    elif amount % 5 == 4:
        coin_amount = (amount//5)+2
    return coin_amount
amount = int(input("Enter an amount to pay: "))
print(f'Minimum number of coins is: {minimum_coin_number(amount)}')