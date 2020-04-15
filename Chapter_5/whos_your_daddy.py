#the purpose of th"nieis program is to take a user input for a son and output the father
tree = {"me": "dad", "Kabochan": "Josh", "Luke": "Anakin", "Alucard": "Dracula"}
choice = ""
son = ""
choice2 = ""
father = ""
while choice != "0":
	print("""

Who's your Daddy?

0 - Exit
1 - Find out who's the father
2 - Add a father and son
3 - Delete a father and son

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
	elif choice == "3":
		choice2 = input("Enter a son to delete its father/son pair: ")
		choice2 = choice2.title()
		if choice2 in tree:
			father = tree[choice2]
			del tree[choice2]
			print(choice2, "and his father", father, "have been deleted.")
	else:
		print("Choice not valid. Try again.")
input("Enter any key to exit: ")
