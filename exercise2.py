name = input("Please enter your name:\n")
number = int(input("Hello {}, please give a random number:\n".format(name)))


if (number % 2 == 0) and (number % 4 == 0):
    print("Even, and also divisable by 4")
elif (number % 2 == 0):
    print("Even")
else:
    print("Odd")

num2 = int(input("Please choose a different number, {}:\n".format(name)))

if (number % num2 == 0):
    print(str(number)+ " is divisable by " +str(num2))
else:
    print(str(number)+ " is not divisable by " +str(num2))
