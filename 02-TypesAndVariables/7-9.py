import random
dice_roll = random.randint(1,6)
valid = dice_roll == 1 or dice_roll == 6
print(f'Dice rolled: {dice_roll}\nSpecial number: {valid}')