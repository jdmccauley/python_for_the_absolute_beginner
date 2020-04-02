#This is a program to showcase modules, with the random module being shown specifically
import random
print('It\'s time to roll some dice.\nWhat number of sided dice do you want to roll?')
dice = int(input('Enter the sided dice you want to roll: '))
print('I\'ll roll the dice for you.')
print('Here is your roll:', random.randint(1,dice))
print('You can roll again, what side dice do you want to roll?')
dice2 = int(input('Enter the sided dice you want to roll: '))
print('Rolling again...')
print('Here is your roll:', random.randrange(dice2) + 1)
input('Press any key to exit.')
