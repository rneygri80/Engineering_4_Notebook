import random

answerlist = []

answer = input("Please type a word player 1:")

print ("\n" * 50)

incorrect = []
def executioner():
    x = ("----","   |", "   O","   |","   |>", "  /|>", "    )", "  / )")

    for stuff in range(0,incorrect):
        if incorrect <= 4:
            print(x[stuff])
        if incorrect == 5:
            if stuff is not 3:
                print(x[stuff])
        if incorrect == 6:
            if stuff is not 3 and stuff is not 4:
                print(x[stuff])
        if incorrect == 7:
            if stuff is not 3 and stuff is not 4:
                print(x[stuff])
        if incorrect == 8:
            if stuff is not 3 and stuff is not 4 and stuff is not 6:
                print(x[stuff])
    

if len(answer) > 1 and answer.isalpha():

    answerlist.append(answer)

    answer = list(answerlist[0])

    display = []

    used = []

    used.extend(display)

    display.extend(answer)

    used.extend(display)

    for i in range (len(display)):
        display[i] = "_"

    print (' '.join(display))
    print()

    count = 0

    incorrect = 3

    while count < len(answer) and incorrect < 9:
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        print (count)

        for i in range(len(answer)):
            if answer[i] == guess and guess in used:
                display[i] = guess
                count = count + 1
                used.remove(guess)

        if guess not in display:
            executioner()
            incorrect = incorrect + 1
            print("sorry, wrong guess")

        print("you have guessed:",count,"correct letters")
        print("you have gotten",int(incorrect - 3),"letters wrong")

        print(' '.join(display))
        print()

    if count == len(answer):

        print("Well done you guessed the word")

    else:
        print("you lost :((((")

else:
    print("you need to type in a word")
