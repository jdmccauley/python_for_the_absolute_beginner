#The purpose of this program is to take in a list of words, and print them in a random order
import random
words = []
words_random = []
choice = ""
addition = ""
sample = 0
while choice != "0":
	print("""
Welcome to the word-list-reorder-inator!
	
0 - Exit
1 - Add a word
2 - Print random order of words
	
	""")
	choice = input("Enter a choice: ")
	if choice == "0":
		print("Good-bye.")
	elif choice == "1":
		addition = input("Enter a word to add: ")
		words.append(addition)
	elif choice == "2":
		while len(words_random) != len(words):
			sample = random.randrange(0, len(words))
			if words[sample] not in words_random:
				words_random.append(words[sample])
		print("Your random order of the word list is: ")
		for i in words_random:
			print("*", i)
		words_random = []
	else:
		print("That is not a valid choice. Please try again.")