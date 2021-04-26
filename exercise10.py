import random


c = random.sample(range(100), random.randint(5,15))
d = random.sample(range(100), random.randint(5,15))

print(c)
print(d)

e = [i for i in c for j in d if i == j]
print(e)
