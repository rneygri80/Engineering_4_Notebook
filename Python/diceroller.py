# Automatic Dice Roller
# Written by Rachel and Claire

from random import randint

print ("Automatic Dice Roller")

min = 1
max = 6

roll_again = "Press enter to roll again"

while roll_again == "Press enter to roll again" or roll_again == "enter":

    print ("Rolling the die...")
    print ("the values are...")
    print (random.randint(min, max))

roll_again = raw_input("Roll the die again?") 
