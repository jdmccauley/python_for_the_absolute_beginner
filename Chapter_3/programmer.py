#This is a program to showcase the if, elif, and else statements
print('Let\'s play a game.\nYou must guess the name of the programmer who wrote this program.')
guess = input('Enter you guess of the name of this programmer: ')
guess = guess.title()
if guess == 'Josh':
    print('Congratulations, you guessed correctly!')
else:
    print('That guess was incorrect, do you want a hint?')
    hint = input('Enter your decision on the hint: ')
    hint = hint.title()
    if hint == 'Yes':
        print('It is one of the McCauley brothers.')
    else:
        print('No hint then.')
    guess2 = input('Enter your second guess of the name of this programmer: ')
    guess2 = guess2.title()
    if guess2 == 'Josh':
        print('Congratulations, you guessed correctly!')
    elif guess2 == 'Kyle':
        print('Wrong brother.')
        guess3 = input('Guess again: ')
        guess3 = guess3.title()
        if guess3 == 'Josh':
            print('Congratulations, you guessed correctly!')
        else:
            print('Wrong brother.')
            guess4 = input('Guess again: ')
            guess4 = guess4.title()
            if guess4 == 'Josh':
                print('Congratulations, you guessed correctly!')
            else:
                print('You could not remember the McCauley brothers. I cannot help with that.')
    elif guess2 == 'Jakob':
        print('Wrong brother.')
        guess3 = input('Guess again: ')
        guess3 = guess3.title()
        if guess3 == 'Josh':
            print('Congratulations, you guessed correctly!')
        else:
            print('Wrong brother.')
            guess4 = input('Guess again: ')
            guess4 = guess4.title()
            if guess4 == 'Josh':
                print('Congratulations, you guessed correctly!')
            else:
                print('You could not remember the McCauley brothers.')
    else:
        print('You could not remember who wrote this program. I cannot help with that.')
input('Press any key to exit.')