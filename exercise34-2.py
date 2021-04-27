# Exercise 34-2

import json

filename = "info.json"

def open_json(filename):
    with open("info.json", "r") as f:
        scientist_birthdays = json.load(f)
    return scientist_birthdays

def add_to_json(file, dictionary):
    user_input = input("Please enter a name (first and last name only) and birthday (DD/MM/YYYY) of a scientist:")
    first_name, last_name, birthday = user_input.split(" ", 3)
    name = first_name + " " + last_name
    dictionary[name] = birthday
    with open(file, "w") as f:
        json.dump(dictionary, f)


def main():
    scientist_birthdays = open_json(filename)
    add_to_json(filename, scientist_birthdays)
    scientist_birthdays = open_json(filename)
    print(scientist_birthdays)


if __name__ == "__main__":
    main()
