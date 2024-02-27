from circle import Circle

circle_1 = Circle(42)
circle_2 = Circle(7)
 
print(circle_1)
print(circle_2)

print("Radius of first circle : ",circle_1.radius)
print("Area of first circle : ", circle_1.calculate_area())

print("Radius of second circle : ", circle_2.radius)
print("Area of second circle", circle_2.calculate_area())