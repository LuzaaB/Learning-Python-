# list
shoplist = ['apple','banana','oranges','mango']

print('I have', len(shoplist), 'items to purchase')

print('These items are:', end=' ')

for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')

print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)



# tuple : same as list but cannot be changed
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo # parentheses not required but are a good idea

print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))



# dictionary : stores only name and address
ab = {
'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org',
'Matsumoto': 'matz@ruby-lang.org',
'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])

del ab['Spammer']# Deleting a key-value pair
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

ab['Guido'] = 'guido@python.org'# Adding a key-value pair

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
    
    
    
# more string functions
name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
    
if 'a' in name:
    print('Yes, it contains the string "a"')
    
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
    
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))