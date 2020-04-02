#This program will showcase the while loop
print('You will soon be visited by a toddler. They do not stop asking \'Why?\'')
print('You must say \'Because.\' to end the infinite questioning.')
print('Toddler: Hello, I am a toddler.\nToddler: I like to understand things.')
answer = ''
print('Toddler: So tell me: ')
while answer != 'Because.':
    print('Toddler: Why?')
    answer = input('You: ')
print('Toddler: Oh. Okay.')
print('The toddler walked away.\nThis simulation is now over.')
input('Press any key to exit.')
