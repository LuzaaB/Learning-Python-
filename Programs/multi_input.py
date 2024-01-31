# Python program showing how to multiple input using split()

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Value of x: ",x)
print("Value of y: ",y)

# taking three inputs at a time
a, b, c = input("Enter three values : ").split()
print("Value of a: ",a)
print("Vallue of b: ",b)
print("Value of c",c)

# taking multiple inputs at a time and type casting using list() function
l = list(map(int, input("Enter multiple values : ").split()))
print("List of numbers: ",l)



# Multiple input using List Comprehension

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is: ",x)
print("Second number is: ",y)

# taking three inputs at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First number is: ",x)
print("Second number is: ",y)
print("Third number is: ",z)

# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ",x)