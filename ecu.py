from car import Car

class ECU:
    def __init__(self, keypassword, car):
        self.correctkeyhex = keypassword
        self.car = car
        try:
            with open("fuel.txt", "r") as file:
                self.car.fuel=int(file.read())  
        except FileNotFoundError:
            self.car.fuel=100


    def unlock_car(self,keyfobsignal):
        if self.correctkeyhex == keyfobsignal:
            self.car.unlock_doors()
        else:
            print("Incorrect key, Access denied")

    def start_engine(self):
        if not self.car.doors_locked and self.car.fuel>0 and self.car.gear=="P":
            self.car.set_engine(True)
        elif self.car.doors_locked:
            print("Cannot start if the door is locked")

        elif self.car.fuel<=0:
            print("Cannot start if there is no fuel")

        elif self.car.gear!="P":
            print("Cannot start the car if the car is not in park")
   