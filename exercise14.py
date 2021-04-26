# Exercise 14

names = ["Jimmy", "Jimmy", "John", "Ryan", "Ryan"]
names_set = set(names)

def remove_duplicates_list(names_list):
    new_names = []
    for i in names_list:
        if i not in new_names:
            new_names.append(i)
    return new_names


duplicates_list = remove_duplicates_list(names)
print(duplicates_list)
