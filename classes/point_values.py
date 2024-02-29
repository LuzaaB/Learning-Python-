from point import ThreePoint

print(ThreePoint.from_sequence((4,8,16)))

point = ThreePoint(7,14,21)
print(point.from_sequence((3,6,9)))

point.show_intro_message("Python Developer")