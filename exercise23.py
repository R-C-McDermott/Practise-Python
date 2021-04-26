# Exercise 23

file_prime_num = "primenumbers.txt"
file_happy_num = "happynumbers.txt"

def read_file(filename):
    with open(filename, 'r') as file:
        list_nums = []
        for nums in file:
            nums_strip = nums.replace("\n", " ").strip()
            list_nums.append(int(nums_strip))
    return list_nums

# Iterates through both number lists and creates a list of duplicates

def create_duplicate_list(first_list, second_list):
    dup_list = []
    for i in first_list:
        for j in second_list:
            if i == j:
                dup_list.append(i)
    return dup_list

def main():
    happy = read_file(file_happy_num)
    prime = read_file(file_prime_num)
    dups = create_duplicate_list(happy, prime)
    print(dups)
    print(len(dups))

if __name__ == '__main__':
    main()
