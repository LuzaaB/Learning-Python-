# Format method is not needed in detail
# Using Format method

print('I love {} for {}'.format('Geek','Geeks'))

# using format() method and referring a position of the object
print('{0} and {1}'.format('Geeks','Portal'))
print('{1} and {0}'.format('Geeks','Protal'))

# shortcut
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")



# using String method - .center .ljust .rjust
cstr = "I love geeksforgeeks"

# Printing the center aligned string 
print("Center aligned string : ")
print(cstr.center(40,'#'))

# Printing the left aligned string
print("Left aligned string : ")
print(cstr.ljust(40,'-'))

# Printing the right aligned string
print("Right aligned string : ")
print(cstr.rjust(40,'-'))