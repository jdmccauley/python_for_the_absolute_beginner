#The purpose of this program is to create an rpg character and assign it attributes
character = {"Name": "", "Race": "", "Gender": "", "Age": 0, "Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}
points = 30
choice = ""
choice2 = ""
choice3 = ""
edit = 0
print("Today you begin your life as an adventurer in Pythonia.")
print("Who are you?")
character["Name"] = input("Enter your name: ")
character["Race"] = input("Enter your race: ")
character["Gender"] = input("Enter your gender: ")
character["Age"] = int(input("Enter your age: "))
print("You are allowed a total of 30 points, how do you want to allocate them?")
print("Here are your choices: Strength, Health, Wisdom, and Dexterity")
while points > 0:
	print("Current attributes:", end = "")
	print("\n", "Strength:", character["Strength"], "\n","Health:", character["Health"], "\n","Wisdom:", character["Wisdom"], "\n","Dexterity:", character["Dexterity"])
	print("""
Enter an attribute to allocate points:
	
0 - Strength
1 - Health
2 - Wisdom
3 - Dexterity

	""")
	choice = input("Enter a choice: ")
	if choice == "0":
		character["Strength"] += int(input("Enter a value to add to Strength: "))
	elif choice == "1":
		character["Health"] += int(input("Enter a value to add to Health: "))
	elif choice == "2":
		character["Wisdom"] += int(input("Enter a value to add to Wisdom: "))
	elif choice == "3":
		character["Dexterity"] += int(input("Enter a value to add to Dexterity: "))
	else:
		print("Choice not valid. Enter a different choice.")
	points = 30 - (character["Strength"] + character["Health"] + character["Wisdom"] + character["Dexterity"])
	if points < 0:
		print("Too many points allocated. Start over.")
		character["Strength"] = 0
		character["Health"] = 0
		character["Wisdom"] = 0
		character["Dexterity"] = 0
choice = None
while choice != "0":
	print("""
Main Menu
	
0 - Begin Journey
1 - View Traits and Attributes
2 - Edit Attributes
3 - Edit Traits
	
	""")
	choice = input("Enter a choice: ")
	if choice == "0":
		print(character["Name"], ", you begin your journey in Pythonia...")
	elif choice == "1":
		print("""
	Traits and Attributes
	
		""")
		for i in character.items():
			print("*", i)
	elif choice == "2":
		print("""
Enter an attribute to decrease:
	
0 - Strength
1 - Health
2 - Wisdom
3 - Dexterity
	
	""")
		choice2 = input("Enter a choice: ")
		edit = int(input("Enter a number of points to remove: "))
		if choice2 == "0":
			character["Strength"] -= edit
		elif choice2 == "1":
			character["Health"] -= edit
		elif choice2 == "2":
			character["Wisdom"] -= edit
		elif choice2 == "3":
			character["Dexterity"] -= edit
		else:
			print("Choice not valid.")
		print("""
Enter an attribute to increase:
	
0 - Strength
1 - Health
2 - Wisdom
3 - Dexterity
	
		""")
		choice2 = input("Enter a choice: ")
		edit = int(input("Enter a number of points to add: "))
		if choice2 == "0":
			character["Strength"] += edit
		elif choice2 == "1":
			character["Health"] += edit
		elif choice2 == "2":
			character["Wisdom"] += edit
		elif choice2 == "3":
			character["Dexterity"] += edit
		else:
			print("Choice not valid.")
		if points < 0:
			print("Too many points allocated. Start over.")
			character["Strength"] = 0
			character["Health"] = 0
			character["Wisdom"] = 0
			character["Dexterity"] = 0
	elif choice == "3":
		print("""
Enter an trait to edit:
	
0 - Name
1 - Race
2 - Gender
3 - Age
	
		""")
		choice2 = input("Enter a choice: ")
		if choice2 == "0":
			character["Name"] = input("Enter a new name: ")
		elif choice2 == "1":
			character["Race"] = input("Enter a new race: ")
		elif choice2 == "2":
			character["Gender"] = input("Enter a new gender: ")
		elif choice2 == "3":
			character["Age"] = input("Enter a new age: ")
		else:
			print("Choice not valid. Enter a different choice.")
	else:
		print("Choice not valid. Enter a different choice.")
input("Enter any key to exit: ")