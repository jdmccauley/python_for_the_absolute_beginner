#This program is a challenge in the book to simulate a fortune cookie.
#The goal is to display one of five fortunes each time it is run.

import random
fortune_1 = "You will live a very happy life and you will die alone."
fortune_2 = "You will try to make a fortune and lose it all."
fortune_3 = "You will find someone to fall in love with, and then you will never act on it."
fortune_4 = "You will throw this fortune away."
fortune_5 = "You will start believing in fortunes from fortune cookies."

print("Waiter: I hope you enjoyed your meal!\nHere is a fortune cookie.")
print("Waiter: If you don't pay before you leave, then I will never let you eat here again.")
print("...you open your fortune cookie...")
fate = random.randint(1,5)
if fate == 1:
    fate = fortune_1
elif fate == 2:
    fate = fortune_2
elif fate == 3:
    fate = fortune_3
elif fate == 4:
    fate = fortune_4
elif fate == 5:
    fate = fortune_5
else:
    fate = "You open a fortune cookie with no fortune."
print("Your fortune reads:\n", fate)
print("...you think about what the fortune cookie means...")
print("Waiter: Where is your payment?!")
input("Enter any key to exit.")
