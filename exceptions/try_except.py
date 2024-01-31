# Exception handler
try :
    text = input("Enter something -->")
except EOFError:
    print("This is an EOF")
except KeyboardInterrupt:
    print("You cancelled operation")
else :
    print(f"You entered {text}")