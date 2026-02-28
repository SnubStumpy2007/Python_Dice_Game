import random

print("welcome to the dice rolling game")
print("1.  Roll the dice")
print("2.  Exit")


selection = input()
if selection == "1":
    print("rolling dice")
    dice = [1, 2, 3, 4, 5, 6]
    roll = random.choice(dice)
    print(roll)
else:
    exit()
