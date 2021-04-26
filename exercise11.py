def get_integer(help_text = "Give me a number:"):
    return int(input(help_text))

def primeValue():
    if len(divisibles) == 1:
        print (str(number) + " is prime")
    else:
        print(str(number) + " is not prime")

number = get_integer()
factors = range(2, number+1)
divisibles = []

for i in factors:
    if number % i == 0:
        divisibles.append(i)

primeValue()
