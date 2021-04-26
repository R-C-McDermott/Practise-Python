# Exercise 20


my_list = [1, 2, 5, 7, 11, 15, 21, 33]

def check_if_value_in_list(some_list, number_check):
    while len(some_list) > 1:
        middle_val = some_list[int(len(some_list)/2)]
        if middle_val > number_check:
            some_list = some_list[0:int(len(some_list)/2)]
        else:
            some_list = some_list[int(len(some_list)/2):len(some_list)]
    if some_list[0] == number_check:
        print("Number is in the list!")
    else:
        print("Number not in list!")


if __name__ == "__main__":
    check_if_value_in_list(my_list, 7)
