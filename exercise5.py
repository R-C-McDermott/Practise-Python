import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


while len(a) < len(b):
    a.append({})

else:
    if len(a) > len(b):
        b.append({})

print(len(a))
print(len(b))

c = []

for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)
d = []
for i in c:
    if i not in d:
        d.append(i)

print(d)

list1 = random.sample(range(30), 6)
list2 = random.sample(range(30), 9)

print(list1)
print(list2)

while len(list1) < len(list2):
    list1.append({})

else:
    if len(list1) > len(list2):
        list2.append({})

print(list1)
print(list2)

e = []

for i in list1:
    for j in list2:
        if i == j:
            e.append(i)
print(e)

f = []
for i in e:
    if i not in f:
        f.append(i)

print(f)
