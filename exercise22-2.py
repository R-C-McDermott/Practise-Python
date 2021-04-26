# Exercise 22 - Extra

file_name = 'Training_01.txt'

# Reading the text file and stripping \n and sorting into list

def read_file(filename):
    with open(filename, 'r') as txt_names:
        list_names = []
        for name in txt_names:
            name_strip = name.replace("\n", " ").strip()
            list_names.append(name_strip)
    return list_names

def parse_file(file_list):
    parsed_list = []
    for title in file_list:
        lhs, rhs = title.split("sun_", 2)
        parsed_list.append(lhs)
    return parsed_list

def remove_duplicates_list(parse_list):
    categories = []
    for i in parse_list:
        if i not in categories:
            categories.append(i)
    return categories

# Iterating through list of names to count how many of each name

def category_count(list_of_parses, categories):
    category_counts = []
    i = 0
    while i < len(categories):
        category_counts.append(list_of_parses.count(categories[i]))
        i += 1
    return category_counts

if __name__ == '__main__':
    file = read_file(file_name)
    parsed_file = parse_file(file)
    categories = remove_duplicates_list(parsed_file)
    category_counts = category_count(parsed_file, categories)
    for j in range(len(categories)):
        print(f"{categories[j]}: {category_counts[j]}\n")
