# Exercise 33

birthday_dictionary = {

"Richard Feynman": "11/05/1918",
"Albert Einstein": "14/03/1879",
"Isaac Newton": "04/01/1643",
"Stephen Hawking": "08/01/1942",
"Nikola Tesla": "10/07/1856"

}


def choose_birthday():
    choice = input("Please select the scientists birthday you would like to know:\n>")
    while choice not in birthday_dictionary.keys():
        print("Sorry, we do not have that birthday. Please try again:")
        choose_birthday()
    return choice

def get_birthday(choice, dictionary):
    return birthday_dictionary[choice]


def main():
    print("Hello! Welcome to the birthday dictionary. We have the following birthdays on record:")
    for i in birthday_dictionary.keys():
        print(i)
    choice = choose_birthday()
    birthday = get_birthday(choice, birthday_dictionary)
    print(f"the birthday of {choice} is {birthday}")

    #print(birthday_dictionary.keys())


if __name__ == '__main__':
    main()
