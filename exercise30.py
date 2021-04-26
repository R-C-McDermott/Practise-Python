# Exercise 30

import random

filename = "sowpods.txt"

# function to read text file, create list of values within file and return random element in list
def choose_random_word(filename):
    word_list = []
    with open(filename, 'r') as f:
        for i in f:
            word_list.append(i)
    return word_list[random.randint(0, len(word_list))]

def main():
    rand_word = choose_random_word(filename)
    print(rand_word)

if __name__ == '__main__':
    main()
