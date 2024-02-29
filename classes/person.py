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