print("Hello!")
name = input("What is your name?\n")
age = int(input("What is your age?\n")).format(name.title())
year = int(input("What year is it?\n"))
year100 = str((year-age)+100)
print(name +", you will be 100 years old in " +year100)
