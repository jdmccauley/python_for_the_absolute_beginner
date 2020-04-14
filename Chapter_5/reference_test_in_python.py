#This is a test of how references work in python.
print("This is a test of references that python uses.")
print("""
	Immutable variable types
	"""
)
a = 1
b = a
c = 1
print("This is the value of a (given 1): ", a)
print("This is the value of b (given a): ", b)
print("This is the value of c (given 1): ", c)
print("This is the address of a: ", id(a))
print("This is the address of b: ", id(b))
print("This is the address of c: ", id(c))
b = 2
c = 2
print("This is the value of a (unchanged): ", a)
print("This is the new value of b (given 2): ", b)
print("This is the new value of c (given 2): ", c)
print("Note that the value of a does change when b is changed.")
print("This is the address of a: ", id(a))
print("This is the address of b: ", id(b))
print("This is the address of c: ", id(c))
print("""
	Mutable variable types
	"""
)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("This is the value of a (given 1, 2, 3): ", a)
print("This is the value of b (given a): ", b)
print("This is the value of c (given 1, 2, 3): ", c)
print("This is the address of a: ", id(a))
print("This is the address of b: ", id(b))
print("This is the address of c: ", id(c))
b.append(4)
c.append(4)
print("This is the value of a (unchanged): ", a)
print("This is the new value of b (edited 1, 2, 3, 4): ", b)
print("This is the new value of c (edited 1, 2, 3, 4): ", c)
print("Note that the value of a does change when b is changed.")
print("This is the address of a: ", id(a))
print("This is the address of b: ", id(b))
print("This is the address of c: ", id(c))