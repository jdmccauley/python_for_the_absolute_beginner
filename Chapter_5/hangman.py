#The purpose of this program is to make a hangman game to showcase dictionaries, tuples, and lists
import random
#ASCII art
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

WORDS = ["python", "hangman", "test", "tuple", "game"]
wrong = 0
guesses = []
choice = None
word = random.choice(WORDS)
print("word is", word, "word type is", type(word))
word_list = []
for letter in word:
	print("letter is", letter)
	word_list.append(letter)
print("word list = ", word_list)
progress = "-" * len(word)
user_progress = ["-"] * len(word)
difference = len(HANGMAN) - len(word)
points = HANGMAN[(difference-1):]
loss = len(word)
counter = 0
status = 0
while counter != loss:
	print(points[counter])
	print("Your guesses are: ")
	i = 0
	for i in guesses:
		print(i, end = "")
	print("\n")
	print("Your progress is: ", progress) 
	choice = input("Enter a letter to guess: ")
	if choice in word and choice not in progress:
		guesses.append(choice)
		print("You correctly guessed a letter in the word.")
		for i in range(len(word_list)):
			if choice == word_list[i]:
				user_progress[i] = choice
				progress = ''.join(user_progress)
	else:
		print("You guessed incorrectly.")
		guesses.append(choice)
		counter += 1
	if progress == word:
		counter = loss
		print("You win!")
	elif counter == loss:
		print(points[counter])
		print("You lose.")
	