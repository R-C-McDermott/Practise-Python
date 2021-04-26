# Exercise 25

import random
import numpy as np


def create_list_of_nums(x,y):
    nums_to_guess = [i for i in range(x,y+1)]
    return nums_to_guess

def computer_guess(list_of_possibilities):
    game_count = 0
    full_list = list_of_possibilities
    while len(list_of_possibilities) > 1:
        guess = list_of_possibilities[random.randint(0, len(list_of_possibilities))]
        print(f"Is your secret number {guess}? (respond 'h' for too high, 'l' for too low and 'c' for correct)\n")
        high_low = input(">")
        if high_low == "l":
            list_of_possibilities = full_list[guess:max(list_of_possibilities)]
            print(list_of_possibilities)
            game_count += 1
        if high_low == "h":
            list_of_possibilities = full_list[min(list_of_possibilities)-1:guess-1]
            print(list_of_possibilities)
            game_count += 1
        if high_low == "c":
            print(f"I win! Your number was {guess}! It took {game_count} guesses!")
            break
    if len(list_of_possibilities) == 1:
        print(f"I win! Your number was {list_of_possibilities[0]}! It took {game_count} guesses!")


def main():
    input_user = input("Please select range of numbers to guess (in format: 'first_number second_number'):\n>")
    start_r, end_r = input_user.split(" ", 2)
    start_r = int(start_r)
    end_r = int(end_r)
    print("Creating list...")
    nums_to_guess = create_list_of_nums(start_r, end_r)
    print("...done!")
    print(nums_to_guess)
    computer_guess(nums_to_guess)




if __name__ == '__main__':
    main()
