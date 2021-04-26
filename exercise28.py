# Exercise 28


def check_largest():
    user_input = input("Please enter 3 numbers (format: num_1 num_2 num_3):")
    first_num, second_num, third_num = user_input.split(" ", 3)
    first_num, second_num, third_num = int(first_num), int(second_num), int(third_num)
    # check largest of first and second num
    if first_num > second_num:
        largest_num = first_num
    else:
        largest_num = second_num
    # Check third num
    if third_num > largest_num:
        largest_num = third_num
    return largest_num


def main():
    largest = check_largest()
    print(largest)

if __name__ == '__main__':
    main()
