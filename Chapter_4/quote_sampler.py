#This program is a demonstration of string indexing.
import random
print("We are going to randomly access characters in a quote that you provide.")
samples = int(input("Enter a number of samples you want to take: "))
quote = str(input("Enter a quote to sample from:\n"))
high = len(quote)
i = 1
j = 0
for i in range(i, samples+1):
    j = random.randrange(-high+1, high)
    print("Character sampled: ", quote[j], "\tThe position is: ", j)
#Note that random.randrange does not include previous random ints, while random.randint does
input("Enter any key to exit:")
