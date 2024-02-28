from shapes import Circle, Square

circle = Circle(100)
print(f"Radius of circle : {circle.radius}")

circle.radius = 500
print(f"Changed radius : {circle.radius}")

circle.radius = 0
print(circle.radius)

square = Square(50)
print(f"Length of the square : {square.side}")

square.side = 25
print(f"Changed length : {square.side}")

square.side = 0
print(square.side)