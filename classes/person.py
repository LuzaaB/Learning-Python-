# Getter and Setter methods
class Person1:
    def __init__(self, name) -> None:
        self.name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        
# Property method - Pythonic Way
class Person:
    def __init__(self, name) -> None:
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value.upper()
        
        
# Values
jane = Person("Jane")
print(jane.name)

jane.name = "Jane Doe"
print(jane.name)

john = Person1("John")
print(john.get_name())

john.set_name("John Doe")
print(john.get_name)