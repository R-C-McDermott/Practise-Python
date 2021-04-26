# Exercise 31
import string

word_to_guess = "GLASGOW"
alph = string.ascii_uppercase

def player_guess():
    guess = input("Guess a letter (upper-case):\n>")
    return guess

def draw_game(word_to_guess):
    print("Welcome to Hang-man!\n***********")
    print("You have 8 guesses!\n***********")
    print(f"Your word contains {len(word_to_guess)} letters and is a City in the UK\n***********")
    game = ["_"]*len(word_to_guess)
    for i in range(0, len(word_to_guess)):
        print(game[i], end = ' ')
    print("\n")
    return game


def guess_check(guess, word):
    correct = [pos for pos, char in enumerate(word) if char == guess]
    return correct

def update_game(game, correct_elements, guess):
    for i in correct_elements:
        game[i] = guess
    for j in range(0, len(game)):
        print(game[j], end = ' ')
    print("\n")
    return game


def main():
    game = draw_game(word_to_guess)
    play = True
    turn = 0
    correct_guesses = 0
    while play == True:
        guess = player_guess()
        while guess in game:
            print("You have already guessed that. Please try again:")
            guess = player_guess()
        while len(guess) > 1:
            print("Too many values, expected 1. Please try again:")
            guess = player_guess()
        while guess not in alph:
            print("Invalid input. Please try again:")
            guess = player_guess()
        while guess == "":
            print("Invalid input. Please try again:")
            guess = player_guess()
        correct = guess_check(guess, word_to_guess)
        game = update_game(game, correct, guess)
        turn += 1
        print(f"Guesses remaining: {8-turn}")
        correct_guesses += len(correct)
        if correct_guesses == len(word_to_guess):
            print(f"Congratulations, you win! You took {turn} turns")
            play = False
        if turn == 8:
            print("Out of turns!")
            play = False

    play_again = input("Would you like to play again? (y/n):\n>")
    while play_again != "y" and play_again != "n":
        print("Invalid input")
        play_again = input("Would you like to play again? (y/n):\n>")
    if play_again == "y":
        main()
    if play_again == "n":
        pass


if __name__ == '__main__':
    main()
