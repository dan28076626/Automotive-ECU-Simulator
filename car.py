class Car:
    def __init__(self):
        self.doors_locked = True
        self.engine_running = False
        self.fuel=100 # %
        self.odometer = 0 # miles
        self.rpm = 0
        self.speed = 0 # miles
        self.gear = "P"
        self.max_speed=217 #km/h
        self.seconds_per_mph=0.0452 # mph
        self.time_scale=2 
        self.mpg=15.7
        self.tank_capacity=18.26 # gallons
        self.decel_seconds_per_mph = 0.5 # mph
        self.max_braking_decel=12.5 # m/s^2
        self.max_rpm=8500 #RPM

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
    # ====== ACCELERATION TIME CALCULATION ======

         # --- Speed Change (mph) ---
        speed_change=target_speed-self.speed

        #--- Acceleration Time (seconds) ---
        accel_time_sec=speed_change*self.seconds_per_mph

    # ==================================================

    # ====== DISTANCE CALCULATION (miles) ======

        # --- Average speed (mph) ---
        average_speed=(target_speed+self.speed) / 2

        # --- Convert acceleration time to hours ---
        accel_time_hour=accel_time_sec/3600

        # --- Final Distance Calculation --- 
        distance=average_speed*accel_time_hour

    # ===========================================
        # --- Update Values --- 
        self.speed=target_speed
        self.odometer+=distance
        self.fuel_used(distance)

    def fuel_used(self,distance):
        # --- Find gallons left in the tank ---
        gallons_left=self.tank_capacity*(self.fuel/100)

        # --- Find the maximum distance the car can travel ---
        maximum_distance=gallons_left*self.mpg

        # --- Check whether the car can travel the distance (dependent on the user's input + fuel in the car) ---
        if distance>maximum_distance:
            print("Car stalled : fuel reached 0%")
            self.fuel=0
            self.engine_running=False
            self.speed=0
            self.rpm=0
            with open("logs/fuel.txt", "w") as file:
                file.write(str(self.fuel))
            return maximum_distance
        # --- Calculate fuel used if the car can make the distance ---
        else:
            gallons_used=distance/self.mpg
            percentage_used=(gallons_used/self.tank_capacity)*100
            self.fuel-=percentage_used
            with open("logs/fuel.txt", "w") as file:
                file.write(str(self.fuel))
            return distance


    def travel(self,real_seconds):

        # --- Calculate simulated time and convert it to hours ---
        simulated_time=(real_seconds*self.time_scale)/3600

        # --- Calculate Distance Travelled --- 
        distance=self.speed*simulated_time

        # --- Get actual distance travelled ---
        actual_distance=self.fuel_used(distance)

        # --- Update Values ---
        self.odometer+=actual_distance

    def decelerate(self,target_speed):

        # --- Calculate Speed change and deceleration time (Sec)
        speed_change=self.speed-target_speed
        decel_time=speed_change*self.decel_seconds_per_mph

    # ====== DISTANCE CALCULATION ======
        # --- Average Speed ---
        average_speed=(self.speed+target_speed)/2

        # --- Convert Deceleration Time per Hours ---
        decel_time_hours=decel_time/3600

        # --- Distance Travelled ---
        distance=average_speed*decel_time_hours

        # --- Update Values ---
        self.odometer+=distance
        self.fuel_used(distance)
        self.speed=target_speed
    # ===============================================

    def braking(self,brake_pressure, target_speed):
        # --- Brake Pressure as a decimal ---
        act_brakepressure=brake_pressure/100

        # --- Find actual deceleration in m/s ---
        act_decel=self.max_braking_decel*act_brakepressure

    # ====== VELOCITY CALCULATION ======
        # --- Convert current speed and target speed to m/s ---
        current_speed_ms=(self.speed*1609.344)/3600 # m/s
        target_speed_ms=(target_speed*1609.344)/3600 # m/s

        # --- Find velocity change ---
        velocity_change=current_speed_ms-target_speed_ms


    # ======================================================

    # ====== BRAKE DISTANCE CALCULATION ======

        # --- Find Brake Time ---
        braking_time=velocity_change/act_decel

        # --- Find average velocity ---
        average_velocity=(current_speed_ms+target_speed_ms)/2

        # --- Distance Travelled (meters) ---
        distance_m=average_velocity*braking_time

        # --- Convert Distance Travelled to miles ---
        distance_miles=distance_m/1609.344

    # ============================================================

        # --- Update Values ---
        self.odometer+=distance_miles
        self.speed=target_speed
        

        


    

        
