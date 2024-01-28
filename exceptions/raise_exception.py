# Raising exception
class ShortInputException(Exception) :
    '''A user defined exception class'''
    def __init__(self, length, atleast) :
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
        
try :
    text = input("Enter somethin -->")
    if len(text) < 3 :
        raise ShortInputException(len(text), 3)
    # Other work can continue as usual here

except EOFError :
    print("EOF has occured")
except ShortInputException as ex:
    print(f"ShortInputException: the input was {ex.length} long, expected atleast {ex.atleast}")

else :
    print("No exceptions were raised.")