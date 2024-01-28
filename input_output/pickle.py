# Python provides a standard module called pickle which you can use to store any Python object in a file
# and then git it back later. This is called the object persistently

import pickle

# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple','mange','carrot']

# Write to the file     
f = open(shoplist,"wb")
# Dum the object to a file
pickle.dump(shoplist, f)
f.close()

# Delete the shoplist variable
del shoplist

# Read back from the storage 
f = open(shoplist, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
f.close()