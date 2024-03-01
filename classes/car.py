class Car:
    def __init__(self, make , model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200
        
    # Example of Instance Method
    def start(self):
        print("Starting the car ...")
        self.started = True
    
    def stop(self):
        print("Stopping the car ...")
        self.started = False
        
    def accelerate(self, value):
        if not self.started:
            print("Car has not started!")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f"Accelerating to {self.speed} km/h...")
        
    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f"Braking to {self.speed} km/h...")
        
    def __str__(self) -> str:
        return f"{self.make}, {self.model}, {self.color}: ({self.year})"
    
    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}"
            f'(make = "{self.make}", '
            f'model = "{self.model}", '
            f"year = {self.year}, "
            f'color = "{self.color}")'
        )
        
        
# Values
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