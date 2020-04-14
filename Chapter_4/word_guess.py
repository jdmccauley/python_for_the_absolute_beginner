#The purpose of this program is to pick a random word,
#tell the user the number of letters in the word,
#have the user guess letters in the word five times
#then have the user guess the word.
import random
word_bank = ("book", "puzzle", "algorithm", "table", "chart", "chest", "note", "python", "script")
word = random.choice(word_bank)
guesses = 0
guess = ""

print("This is a game where you will guess a word.\nYou will get the number of letters in the word, and get to guess letter in the word five times.")
print("Let's begin. Your selection of words is:")
for i in word_bank:
	print("*", i)
print("Picking a word...")
print("The number of letters in the word is:", len(word))
while guesses != 5:
	guess = input("Enter a letter to guess if it is in the word: ")
	guess = guess.lower()
	if guess in word:
		print("Yes.")
	else:
		print("No.")
	guesses += 1
answer = input("Enter your guess for the word: ")
if answer == word:
	print("Congradulations, you guessed the word.")
else:
	print("You guessed incorrectly. Try again later.")
input("Enter any key to exit.")
