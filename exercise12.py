import random

def createRandomList():
    a = list(random.sample(range(20), random.randint(1,30)))
    return a

def createNewList():
    b = []
    b.append(firstList[0])
    b.append(firstList[-1])
    return b

firstList = createRandomList()
print(firstList)

new = createNewList()
print(new)
