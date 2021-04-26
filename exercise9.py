import random

play = True
while play:
    randnumber = random.randint(1, 9)
    print(randnumber)

    numberOfGuesses = 1

    while True:
        guess = input("Guess the number:\n")
        if guess == "quit":
            play = False
            break
        elif int(guess) == randnumber:
            print("Correct! You took " + str(numberOfGuesses) + " guesses to answer correctly")
            break
        else:
            numberOfGuesses += 1
            print("Guess again!")
