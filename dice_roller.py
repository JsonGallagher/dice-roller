from random import randint
print("Welcome to dice roller")
print()
num_dice = int(input("How many dice are we rolling? "))
num_sides = int(input("How many sides on each die? "))

while True:
    result = "| "
    for i in range(num_dice):
        roll = randint(1,num_sides)
        result += f"{roll} | "
    print(f"You rolled: {result}")
    roll_again = input("Roll again? ('q' to quit) ")
    if roll_again == 'q':
        break