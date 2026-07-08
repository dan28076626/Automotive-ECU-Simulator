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

   