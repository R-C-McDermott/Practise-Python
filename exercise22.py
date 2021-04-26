# Exercise 22

#file_name_names = 'nameslist.txt'
file_name_names = 'nameslist2.txt'

# Reading the text file and stripping \n and sorting into list

def read_file(filename):
    with open(filename, 'r') as txt_names:
        list_names = []
        for name in txt_names:
            name_strip = name.replace("\n", " ").strip()
            list_names.append(name_strip)
    return list_names

# Remove duplicates from list of names to show which names are in the text file

def remove_duplicates_list(names_list):
    names_in_file = []
    for i in names_list:
        if i not in names_in_file:
            names_in_file.append(i)
    return names_in_file

# Iterating through list of names to count how many of each name

def name_count(list_of_names, names_contained):
    name_counts = []
    i = 0
    while i < len(names_contained):
        name_counts.append(list_of_names.count(names_contained[i]))
        i += 1
    return name_counts

# main function

if __name__ == '__main__':
    list_names = read_file(file_name_names)
    names_contained = remove_duplicates_list(list_names)
    count_of_names = name_count(list_names, names_contained)
    for j in range(len(names_contained)):
        print(f"{names_contained[j]}: {count_of_names[j]}\n")
