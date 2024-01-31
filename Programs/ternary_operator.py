# Simple way
a, b = 10, 20
min = a if a < b else b
print(min)

# Ternary operator in if-else
# Native way
a, b = 10, 20
if a!=b :
    if a<b :
        print("a is lesser than b")
    else :
        print("a is greater than b")
else :
    print("Both a and b are equal")
    
# Ternary way
a, b = 10, 20
print("Both a and b are equal" if a==b else "a is greater than b" if a>b else "a is lesser than b")

# Ternary operator using Tuple
a, b = 10, 20
print( (a,b) [a<b])
""" if [a<b] is true it returns 1, so element with index 1 will print
    else if [a<b] is false it returns 0, so element with index 0 will print """

# Ternary operator using Dictionary
a, b = 10, 20
print({True: a, False: b} [a<b])

# print in ternary
a, b = 5, 7
print(a,"is greater") if (a>b) else print(b,"is greater")