# Exercise 15


def reverse_string(user_string):
    user_input_split = user_string.split()
    user_string_reversed_list = list(reversed(user_input_split))
    user_input_reversed = " ".join(user_string_reversed_list)
    return user_input_reversed

user_input = input("Please give a sentence:\n>")

print(reverse_string(user_input))
