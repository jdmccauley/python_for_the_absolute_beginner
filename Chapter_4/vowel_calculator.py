#The purpose of this program is to demonstrate the use of the 'in' operator.
print("Let's calculate the number of vowels in a quote you write.")
quote = str(input("Enter a quote to analyze: "))
print("Analyzing sequence...")
a = 0
e = 0
i = 0
o = 0
u = 0
for letter in quote:
    if letter == "a" or letter == "A":
        a += 1
    elif letter == "e" or letter == "E":
        e += 1
    elif letter == "i" or letter == "I":
        i += 1
    elif letter == "o" or letter == "O":
        o += 1
    elif letter == "u" or letter == "U":
        u += 1
print("The number of each vowel in your quote is:\nA = ", a, "\nE = ", e, "\nI = ", i, "\nO = ", o, "\nU = ", u)
input("Enter any key to exit: ")
