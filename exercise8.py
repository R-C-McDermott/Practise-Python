play = True
while play:
    while True:
        choice = ["rock", "paper", "scissors"]
        Player1 = input("Player 1 enter choice:\n")
        Player1 = Player1.lower()
        if Player1 in choice:
            break
        else:
            print("Wrong input")


    while True:
        choice = ["rock", "paper", "scissors"]
        Player2 = input("Player 2 enter choice:\n")
        Player2 = Player2.lower()
        if Player2 in choice:
            break
        else:
            print("Wrong input")

    if Player1 == Player2:
        print("Stale-mate!")
    elif (Player1 == "rock") and (Player2 == "scissors"):
        print("Player 1 wins!")
    elif (Player1 == "rock") and (Player2 == "paper"):
        print("Player 2 wins!")
    elif (Player1 == "scissors") and (Player2 == "rock"):
        print("Player 2 wins!")
    elif (Player1 == "scissors") and (Player2 == "paper"):
        print("Player 1 wins!")
    elif (Player1 == "paper") and (Player2 == "scissors"):
        print("Player 2 wins!")
    elif (Player1 == "paper") and (Player2 == "rock"):
        print("Player 1 wins!")

    again = input("Would you like to play again? [yes/no]:\n")
    again = again.lower()

    if again == "no":
        print("Goodbye!")
        break
    else:
        play == True
