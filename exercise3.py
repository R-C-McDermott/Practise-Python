a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print (i)

newlist = list(filter(lambda b: b < 5, a))
print(newlist)

usernum = int(input("Please give a number:\n"))

userlist =list(filter(lambda j: j < usernum, a))
print(userlist)
