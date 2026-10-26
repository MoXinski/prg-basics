import math

def negative_even(x, y):
    if x>=-1:
        return 0
    else:
        n1 = (math.sqrt(x**2))//2
        n2 = y//2
        if n1>n2:
            return n2
        else:
            return n1

x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(int(negative_even(x, y)))