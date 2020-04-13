#Word Jumble
#
#The computer picks a random word and then "jumbles" it
#The player has to guess the original word
import random
#create sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "Xylophone")
#pick one word randomly from the sequence
word = random.choice(WORDS)
#create a variable to use later to see if the guess is correct
correct = word
jumble = ""
#jumble the word until 
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
#start the game
print(
"""
            Welsome to Word Jumble!
            
        Unscramble the letters to make a word.
    (Press any key at the prompt to quit.)
"""
)
print("The word jumble is:", jumble)
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it!. You guessed it!\n")

print("Thanks for playing.")
input("\nPress the enter key to exit.")
