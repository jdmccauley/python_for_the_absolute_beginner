#The purpose of this program is to demonstrate a for loop with range().
print("This is an example of a 'for' loop.")
print("What number of you want to count to?")
number = int(input("Enter the number you want to count to: "))
start = int(input("Enter the number you want to start with: "))
iteration = int(input("Enter the amount you want to iterate by: "))
print("Counting...")
for i in range(start, number+1, iteration):
    print(i)
input("Enter any key to exit: ")
