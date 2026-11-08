def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

print(f'Sum of natural numbers in the range <1,10> is {sum_natural(10)}')
