#Word Jumble
#
#The computer picks a random word and then "jumbles" it
#The player has to guess the original word
import random
#create sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "Xylophone")
HINT = ("The language this game was written in.", "What this games does to words.", "A word for not hard.", "A word for not easy.", "What you give to a question.",
        "An instrument that starts with the letter X.")

#pick one word randomly from the sequence
selection = random.randrange(0,len(WORDS))
word = WORDS[selection]
hint = HINT[selection]
#create a variable to use later to see if the guess is correct
correct = word
jumble = ""
#jumble the word until 
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
#start the gamei
guess_count = 0
hint_count = 0
hint_choice = ""
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
    hint_choice = input("Do you want a hint? If so, enter 'Y': ")
    if hint_choice == 'Y':
        hint_count += 1
        print("Your hint is:", hint)
    guess = input("Your guess: ")
if guess == correct:
    print("That's it!. You guessed it!\n")
if hint_count == 0:
    print("And you guessed without any hints!")
    print("""
C O N G R A D U L A T I O N S
You're really smart! Wow! Fantastic!
        """)

print("Thanks for playing.")
input("\nPress the enter key to exit.")
