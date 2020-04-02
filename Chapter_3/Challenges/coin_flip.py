#The goal of this program is to flip a coin 100 times, and tell the number of heads and tails flipped.
import random

print("We will flip a coin 100 times.")
flip = 1
heads = 0
tails = 0
chance = 0
while flip != 100:
	chance = random.randint(0,1)
	if chance == 0:
		heads = heads + 1
	if chance == 1:
		tails += 1
	#else:
	#	print("Failure.")
	#The 'else' condition runs every time that the 'while' loop is FALSE
	flip += 1
print("The number of heads you got was: ", heads)
print("The number of tails you got was: ", tails)
input("Enter any key to exit.")
