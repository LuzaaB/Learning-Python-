from car import Car

toyota_camry = Car("Toyota", "Camry", 2024, "Blue")
print("Model of the first car :",toyota_camry.model)
print("Manufacture Year of the first car :",toyota_camry.year)
print("Company Name of the first car :",toyota_camry.make)
print("Speed of the first car :",toyota_camry.speed)

ford_mustang = Car("Ford", "Mustang", 1998, "Black")
print("Company Name of the second car : ",ford_mustang.make)
print("Model of the second car : ",ford_mustang.model)
print("Manufactured Year Name of the second car : ",ford_mustang.year)
print("Max Speed of the second car : ",ford_mustang.max_speed)

print(ford_mustang.accelerate(100))
print(ford_mustang.brake(50))
print(ford_mustang.brake(80))
print(ford_mustang.stop())
print(ford_mustang.accelerate(100))


""" Manually providing the instances """
print(Car.start(ford_mustang))
print(Car.accelerate(ford_mustang, 200))
print(Car.brake(ford_mustang, 100))
print(Car.stop(ford_mustang))

# str(toyota_camry) - use in terminal directly
print(toyota_camry)

# toyota_camry - use in terminal directly
print(repr(toyota_camry))