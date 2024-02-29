class Aircraft:
    def __init__(self, thrust, lift, max_speed) -> None:
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed
        
    def show_techincal_specs(self):
        print(f"Thrust : {self.thrust} kW")
        print(f"Lift : {self.lift} kg")
        print(f"Max Speed : {self.max_speed} km/h")
        
class Helicopter(Aircraft):
    def __init__(self, thrust, lift, max_speed, num_rotors) -> None:
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors
        
    def show_techincal_specs(self):
        super().show_techincal_specs()
        print(f"Number of rotors : {self.num_rotors}")