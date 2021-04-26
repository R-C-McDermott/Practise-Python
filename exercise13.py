# Exercise 13

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1)+fib(n-2)

#print(fib(8))


number_fib = int(input("How many fibinachi numbers?:\n>"))
fib_Seq = []

i=0
while i < number_fib:
    fib_Seq.append(fib(i))
    i += 1

print(fib_Seq)
