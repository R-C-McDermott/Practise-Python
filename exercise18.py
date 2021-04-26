# Exercise 18
# Cows and Bulls
import random

def create_number_list():
    rand_list = []
    i=0
    while i<4:
        rand_list.append(random.randint(1,9))
        i += 1
    return rand_list

def user_input():
    user_guess = [int(x) for x in input("Guess the random 4 digit number :> ")]
    return user_guess

def cow_and_bull():
    user_num = user_input()
    cows = 0
    bulls = 0
    attempts = 0
    for x in range(4):
        if user_num[x] == comp_num[x]:
            bulls += 1
            attempts += 1
    for y in range(4):
        for z in range(4):
            if user_num[y] == comp_num [z] and user_num[y] != comp_num[y] and user_num[z] != comp_num[z]:
                cows += 1
                attempts += 1
    if bulls == 4:
        print("You have won!")
    else:
        print("Cows:" , cows, "Bulls: ", bulls)
        cow_and_bull()


# Testing list comprehension
def testy():
    test_guess = input("BEEP:")
    test_list = [int(i) for i in test_guess]
    return test_list


if __name__=="__main__":
    print("Welcome to Cows and Bulls!\n\n***********\n")
    print("If you guess the correct number in the correct position you will score a bull!\n")
    print("If you guess a correct number in the incorrect position you will score a cow!\n")
    print("Press CTRL-C to exit any time!\n")
    comp_num = create_number_list()
    cow_and_bull()
