#The purpose of this program is to demonstrate a for loop with range().
print("This is an example of a 'for' loop.")
print("What number of you want to count to?")
number = int(input("Enter the number you want to count to: "))
print("Counting...")
for i in range(1, number+1):
    print(i)
    i+= 1
input("Enter any key to exit: ")
