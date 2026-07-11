from car import Car
from modules.canbus import CANBus

class ECU:
    def __init__(self, keypassword, car,canbus):
        self.correctkeyhex = keypassword
        self.car = car
        self.canbus=canbus
        try:
            with open("fuel.txt", "r") as file:
                self.car.fuel=int(file.read())  
        except FileNotFoundError:
            self.car.fuel=100

    def get_canbus(self):
        for message in self.canbus.messages:
            if message["id"]=="0x101" and not message["processed"]:
                if message["command"]=="UNLOCK_CAR":
                    self.unlock_car(message["data"])
                    message["processed"]=True
                elif message["command"]=="START_ENGINE":
                    self.start_engine()
                    message["processed"]=True
                elif message["command"]=="STOP_ENGINE":
                    self.stop_engine()
                    message["processed"]=True
                elif message["command"]=="SELECT_GEAR":
                    self.select_gear(message["data"])
                    message["processed"]=True
                elif message["command"]=="REFUEL":
                    self.refuel(message["data"])
                    message["processed"]=True
                elif message["command"]=="DRIVE_MILES":
                    self.drive_miles(message["data"])
                    message["processed"]=True
                elif message["command"]=="LOCK_CAR":
                    self.car.lock_doors()
                    message["processed"]=True



    def unlock_car(self,keyfobsignal):
        if self.correctkeyhex == keyfobsignal:
            self.car.unlock_doors()
        else:
            print("Incorrect key, Access denied")

    def start_engine(self):
        if not self.car.doors_locked and self.car.fuel>0 and self.car.gear=="P":
            self.car.set_engine(True)
            print("Car started")
        elif self.car.doors_locked:
            print("Cannot start if the door is locked")

        elif self.car.fuel<=0:
            print("Cannot start if there is no fuel")

        elif self.car.gear!="P":
            print("Cannot start the car if the car is not in park")

    def stop_engine(self):
        if not self.car.engine_running:
            print("Cannot stop the engine if it is already off")
        elif self.car.gear !="P":
            print("Cannot turn the car off if it is in drive")
        else:
            self.car.set_engine(False)
   
    def select_gear(self,gear):

        gear=gear.upper()

        if gear not in ["P", "R", "N", "D"]:
            print("Invalid gear")
        elif not self.car.engine_running:
            print("Cannot shift gears if the engine is not on")
        elif self.car.speed!=0 and self.car.gear=="P":
            print("Cannot switch to park if car is moving")
        else:
            self.car.set_gear(gear)

    def drive_one_mile(self):
        if not self.car.engine_running:
            print("Cannot move if car is not turned on")
        elif self.car.fuel<=0:
            print("Cannot move the car if there is no fuel")
        elif self.car.gear !="D":
            print("Cannot move if car is not in drive")
        else:
            self.car.drive_one_mile()
            with open("fuel.txt", "w") as file:
                file.write(str(self.car.fuel))

    def drive_miles(self,miles):
        if not self.car.engine_running:
            print("Cannot move if car is not turned on")
        elif self.car.fuel<=0:
            print("Cannot move the car if there is no fuel")
        elif self.car.gear !="D":
            print("Cannot move if car is not in drive")
        else:
            for i in range(miles):
                self.drive_one_mile()
                if self.car.fuel<5:
                    print("Does not have enough fuel to drive one more mile")
            with open("fuel.txt", "w") as file:
                file.write(str(self.car.fuel))

    def refuel(self,amount):
        if self.car.engine_running:
            print("Cannot refuel if engine is running")
        elif amount<=0:
            print("Cannot refuel if the value is less than/equal to 0")
        elif self.car.fuel==100:
            print("Fuel tank already full")
        else:
            self.car.refuel(amount)
            self.update_dashboard()
            with open("fuel.txt", "w") as file:
                file.write(str(self.car.fuel))

    def update_dashboard(self):
        self.canbus.send_message("ECU", "DASHBOARD", "UPDATE_FUEL", self.car.fuel)
        self.canbus.send_message("ECU", "DASHBOARD", "UPDATE_RPM", self.car.rpm)
        self.canbus.send_message("ECU", "DASHBOARD", "UPDATE_GEAR", self.car.gear)
        self.canbus.send_message("ECU", "DASHBOARD", "UPDATE_SPEED", self.car.speed)
        self.canbus.send_message("ECU", "DASHBOARD", "UPDATE_ODOMETER", self.car.odometer)
        self.canbus.send_message("ECU", "DASHBOARD", "UPDATE_ENGINE", self.car.engine_running)
        self.canbus.send_message("ECU", "DASHBOARD", "UPDATE_DOORS", self.car.doors_locked)
        
