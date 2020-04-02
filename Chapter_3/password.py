#This is a program to showcase the if and else statements
print('You must guess the password to continue')
guess = input('Enter your password guess: ')
if guess == 'password':
    print('You guessed correct. There is no reward for this.')
else:
    print('You guessed incorrect. Try again next time.')
input('Press any key to continue.')