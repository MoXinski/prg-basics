def f(dice):
    best_number = dice[0]
    best_count = 1
    count = 1
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            count += 1
        else:
            count = 1
        if count > best_count:
            best_count = count
            best_number = dice[i]
    return int(best_number)

print(f('5233165554211'))
print(f('2133'))
