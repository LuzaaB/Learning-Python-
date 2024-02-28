from circle import Circle

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