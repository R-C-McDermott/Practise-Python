word = input("Please enter a word:\n")

wordlen = len(word)
print(wordlen)

revword = ""

for i in reversed(word):
    revword += i
print (revword)

if word == revword:
    print("This is a palindrome")
else:
    print("This isn't a palindrome")
