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
    
    
# Values
circle_1 = Circle(42)
circle_2 = Circle(7)
 
print(circle_1)
print(circle_2)

print("Radius of first circle : ",circle_1.radius)
print("Area of first circle : ", circle_1.calculate_area())

print("Radius of second circle : ", circle_2.radius)
print("Area of second circle", circle_2.calculate_area())

cicrle_3 = Circle(100)
print(f"Radius of third circle : {cicrle_3}")

circle_4 = Circle(0)
print(circle_4)

circle_5 = Circle("200")
print(circle_5)