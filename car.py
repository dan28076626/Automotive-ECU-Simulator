class Car:
    def __init__(self):
        self.doors_locked = True
        self.engine_running = False
        self.fuel=100
        self.odometer = 0
        self.rpm = 0
        self.speed = 0
        self.gear = "P"
        self.max_speed=217
        self.seconds_per_mph=0.0452

    def unlock_doors(self):
        self.doors_locked = False
        print("Car: Doors unlocked")

    def lock_doors(self):
        self.doors_locked = True
        print("Car: Doors locked")

    def set_engine(self, running):
        self.engine_running = True

        if running:
            self.rpm = 800
            print("Car: Engine is now running")
        else:
            self.rpm = 0
            self.speed = 0
            self.gear = "P"
            print("Car: Engine stopped")

    def set_gear(self, gear):
        valid_gears = ["P", "R", "N", "D"]

        if gear in valid_gears:
            self.gear = gear
            print(f"Car: Gear changed to {gear}")
        else:
            print("Car: Invalid gear")

    def drive_one_mile(self):
        if not self.engine_running:
            print("Car: Cannot move, engine is off")
            return

        if self.gear != "D":
            print("Car: Cannot drive, gear is not in Drive")
            return

        if self.fuel <= 0:
            self.engine_running = False
            self.rpm = 0
            self.speed = 0
            print("Car: No fuel. Engine stalled.")
            return
        self.odometer += 1
        self.fuel = max(0, self.fuel - 5)
        self.speed = 30
        self.rpm = 2000

        print(f"Car: Drove 1 mile | Fuel: {self.fuel}% | Mileage: {self.odometer} miles")

    def refuel(self, amount):
        self.fuel = min(100, self.fuel + amount)
        print(f"Car: Refuelled. Fuel is now {self.fuel}%")

    def accelerate(self,target_speed):
       
        speed_change=target_speed-self.speed
        acceleration_time=speed_change*self.seconds_per_mph
        print(speed_change)
        print(acceleration_time)


        
