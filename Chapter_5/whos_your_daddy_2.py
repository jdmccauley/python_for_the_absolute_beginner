#the purpose "of th"nieis program is to take a user input for a son and output the father
tree = {"me": "dad", "Kabochan": "Josh", "Luke": "Anakin", "Alucard": "Dracula"}
tree_2 = ["Donald", "Brad", "nobody remembers his name but hes a farmer", "Lucifer"]
choice = ""
son = ""
choice2 = ""
choice3 = ""
father = ""
index = 0
grandfather = ""
while choice != "0":
	print("""

Who's your Daddy?

0 - Exit
1 - Find out who's the father
2 - Add a father and son, maybe a grandpa too
3 - Delete a father and son
4 - Find a grandfather

	""")
	choice = input("Enter a choice: ")
	if choice == "0":
		print("Thank you for playing \"Who's your Daddy?\" today.")
	elif choice == "1":
		while son not in tree:
			son = input("What is the name of the son's daddy you want to find?\nEnter the son's name here: ")
			son = son.title()
			if son in tree:
				print("The father is:", tree[son])
			else:
				print("Son not known in this repository. Try another son.")
	elif choice == "2":
		son = input("Enter a son to add to the repository: ")
		son = son.title()
		father = input("Enter the father: ")
		father = father.title()
		tree[son] = father
		print(son, "and his father,", tree[son], ", has been added to the repository.")
		son = ""
		father = ""
		choice3 = input("Do you want to enter a grandpa?\nIf so, enter 'Y': ")
		if choice3 == "Y":
			grandfather = input("Enter the name of the grandfather: ")
			tree_2.append(grandfather)
			print("The list of grandfathers has been updated.")
			grandfather = ""
		else:
			print("No grandfather will be added.")
	elif choice == "3":
		choice2 = input("Enter a son to delete its father/son pair: ")
		choice2 = choice2.title()
		if choice2 in tree:
			father = tree[choice2]
			del tree[choice2]
			print(choice2, "and his father", father, "have been deleted.")
	elif choice == "4":
		while son not in tree:
			son = input("What is the name of the son's grandfather you want to find?\nEnter the son's name here: ")
			son = son.title()
			if son in tree:
				for i in tree:
					if i == son:
						print("The grandfather is:", tree_2[index])
					index += 1
		son = ""
		index = 0
	else:
		print("Choice not valid. Try again.")
input("Enter any key to exit: ")
