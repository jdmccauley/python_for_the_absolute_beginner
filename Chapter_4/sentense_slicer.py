#The purpose of this program is to demonstrate slicing strings.
print("Let's slice up a sentense.")
quote = input("Enter a quote to slice: ")
begin = int(input("Enter an index for the beginning of the slice: "))
end = int(input("Enter an index for the end of the slice: "))
if begin <= len(quote) and end <= len(quote):
	print("Your slice is:", quote[begin:end])
else:
	print("Your index was longer than the sentence. Try again later.")
input("Enter any key to exit.")
