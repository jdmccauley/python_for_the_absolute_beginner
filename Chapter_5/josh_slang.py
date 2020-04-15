#The purpose of this program is to showcase dictionaries
slang = {"lmao": "'Laughing my ass off', but not literally. A medium laugh.", "rip": "'Rest in peace', can be said to say when something is lost",
"yeet": "When something is quickly moved from one place to another. Can also mean yes."}
choice = None
words_list = []
while choice != "0":
	print("""
	Welcome to the Josh Slang Dictionary
	
	0 - Exit
	1 - Read a definition of a word
	2 - Add a word
	3 - Delete a word
	
	""")
	choice = input("Enter a choice: ")
	if choice == "0":
		print("Goodbye.")
	elif choice == "1":
		print("The words in the Josh Slang Dictionary are:")
		words_list = slang.keys()
		for i in slang.keys():
			print("*", i)
		term = input("Enter a word you want to define: ")
		if term in slang:
			print(term, ":", slang[term])
		else:
			print("That term is not in the slang dictionary.\nYou can add it by selecting '2' in the menu.")
	elif choice == "2":
		term = input("Enter a word to add to the Josh Slang dictionary: ")
		if term not in slang:
			define = input("Enter a definition of the word: ")
			slang[term] = define
			print("The Josh Slang dictionary has been updated, here is the newest entry:\n", term, ":", slang[term])
		else:
			print("That term is already in the slang dictionary,\nYou can see the definition by selecting '1' in the menu.")
	elif choice == "3":
		term = input("Enter a word to delete from the Josh Slang dictionary: ")
		if term in slang:
			del slang[term]
			print(term, "has been deleted from the Josh Slang dictionary.")
		else:
			print("That term is not yet in the Josh Slang Dictionary.\nYou can add it first by selecting '2' in the menu.")
	else:
		print("That is not a valid selection. Try again.")