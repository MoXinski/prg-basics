def month(n):
    if n==1:
        month_name='January'
    elif n==2:
        month_name='February'
    elif n==3:
        month_name='March'
    elif n==4:
        month_name='April'
    elif n==5:
        month_name='May'
    elif n==6:
        month_name='June'
    elif n==7:
        month_name='July'
    elif n==8:
        month_name='August'
    elif n==9:
        month_name='September'
    elif n==10:
        month_name='October'
    elif n==11:
        month_name='November'
    elif n==12:
        month_name='December'

    return month_name

i = int(input("Enter month number: "))
if i>0 and i<=12:
    print(f'The name of month {i} is {month(i)}')
else:
    print("There are only 12 months.")