
import json

class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __repr__(self):
        return f"Person(Name:{self.name}, Phone-Number:{self.phone})"



class Database:
    def __init__(self):
        self.data = {}
    
    def add_contact(self, name, phone):
        self.data[name] = Person(name, phone)
        
    def delete_contact(self, name):
        pass
    
    def find_by_name(self, name):
        # try:
        #     return self.data[name]
        # except KeyError as e:
        #     return None
        return self.data.get(name, None)
                    
    def find_by_number(self, number):
        for name, person in self.data.items():
            if person.phone == number :
                return name
            
    def print_db(self):
        print(self.data)
    
    

db = Database()
# seed data
db.add_contact("Sanskar", 1234)
db.add_contact("Ganesh", 4557)
db.add_contact("Luzaa", 7500)

running = True
HELP_STRING = "1) ADD : Add a contact\n" \
              "2) FIND: Find by name\n" \
              "3) DEL <name>: Delete a contact\n" \
              "4) PRINT: Print the contents\n" \
              "5) QUIT: Quit\n" \
              "6) HELP: Show this help text\n"
    
    
print("Welcome to Luzaa's Phonebook Program")
print(HELP_STRING)

while running:
    
    ## Take input
    user_inp = input("$ ").strip()
    
    if user_inp == "HELP":
        print(HELP_STRING)
    
    elif user_inp == "ADD":
        inp_name = input("Enter a name : ")
        inp_num = input("Enter phone number : ")
        db.add_contact(inp_name,inp_num)
        
    elif user_inp == "FIND":
        inp_find = input("Enter a name/number to search : ")
        if isinstance(inp_find, int):
            person = db.find_by_number(inp_find)
        else:
            person = db.find_by_name(inp_find)
        if person is None:
            print("Not found")
        else:
            print("FOUND: ", person)        
        # inp_find_num = input("Enter a phone number if you want to search by number")
        # db.find_by_number(inp_find_num)
        # found_num = db.find_by_number()
        # print(found_num,"is PRESENT")
    
    elif user_inp == "DEL":
        inp_del = input("Enter the contact to be deleted : ")
        db.delete_contact()
    
    elif user_inp == "QUIT":
        running = False 
    
    elif user_inp == "PRINT":
        db.print_db
    
    else:
        print("Invalid command. Type HELP for help")