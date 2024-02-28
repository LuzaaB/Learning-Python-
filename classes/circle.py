import math 

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def radius(self):
        return self.radius
    
    @radius.setter
    def radius(self,value):
        if not isinstance(value, int|float) or value <= 0 :
            raise ValueError("Positive number expected")    
        self.radius = value
        
    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)