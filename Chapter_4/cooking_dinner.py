#The purpose of this program is to showcase tuples and how to use them.
#This program will give the user a list of ingredients,
#ask the user what recipe they want to make, and then check if the recipe can be made.
print("It is 7 PM on a Sunday night...\nYou are hungry, and you've already eaten out too many times this week.")
print("You check your kitchen, and you have a mix of random ingredients.")
ingredients = ("flour", "sugar", "eggs", "spaghetti", "tomato sauce",
"bread crumbs", "cheese", "cereal", "eggplant", "ice cream", "butter")
print("The following ingredients are in your kitchen:")
for i in ingredients:
	print("*", i)
print("You decide to look at your cookbook for some ideas.")
input("Enter any key to read your cookbook: ")
print("These recipes look interesting:")
cereal = ( "cereal", "milk")
pound_cake = ("flour", "sugar", "eggs", "butter")
spaghetti_bolognese = ("spaghetti", "tomato sauce", "ground beef")
eggplant_parmesean = ("spaghetti", "tomato sauce", "eggplant", "eggs", "flour", "bread crumbs", "cheese")
print("~Cereal with milk~\nAdd the following ingredients together and enjoy:")
for i in cereal:
	print("*", i)
input("Enter any key to continue reading: ")
print("~Pound cake~\nMix a pound of each and bake at 350F for an hour and 15 minutes:")
for i in pound_cake:
	print("*", i)
input("Enter any key to continue reading: ")
print("~Spaghetti bolognese~\nBoil spaghetti until al dente, brown meat, and heat sauce.")
print("Serve meat and sauce over spaghetti. Uses the following:")
for i in spaghetti_bolognese:
	print("*", i)
input("Enter any key to continue reading: ")
print("~Eggplant parmesean~\nBread eggplant with flour, egg, then bread crumbs. Fry the eggplant.")
print("Boil spaghetti and heat tomato sauce. Serve eggplant on top of spaghetti. Cover with sauce and cheese.")
print("Uses the following ingredients:")
for i in eggplant_parmesean:
	print("*", i)
input("You finish reading the cookbook, it's short.\nEnter any key to stop reading: ")
print("\n\nWhat should you make?")
print("*Use the following codes for each.\nCereal = 1\nPound Cake = 2\nSpaghetti bolognese = 3\nEggplant parmesean = 4*")
choice = int(input("Enter a recipe to cook: "))
if choice == 1:
    dinner = cereal
elif choice == 2:
    dinner = pound_cake
elif choice == 3:
    dinner = spaghetti_bolognese
elif choice == 4:
    dinner = eggplant_parmesean
else:
    print("You choose not to eat. You go to bed hungry.")
success = 0
for i in ingredients:
    if i in dinner:
        success += 1
if success == len(dinner):
    print("You make a successful dinner and go to bed happy.")
else:
    print("You don't have the ingredients to make your choice. You go to bed hungry.")
input("Enter any key to exit: ")