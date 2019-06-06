from random import randint

print ("Do you want to roll? (Y)es or (N)o")
answer = input()
while answer.lower()[0] == "y":
    num1 = randint(1,6)
    print ("You rolled a", num1)
    print ("Do you want to roll? (Y)es or (N)o")
    answer = input()
    
