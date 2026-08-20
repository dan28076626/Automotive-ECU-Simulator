class TCM:
    def __init__(self , car, gearbox, canbus):
        self.car=car
        self.gearbox=gearbox
        self.canbus=canbus

    def upshift(self):
        if self.gearbox.current_gear==7:
            print("Cannot upshift to a gear higher than 7")
        else:
            self.gearbox.upshift()

    def downshift(self):
        if self.gearbox.current_gear==1:
            print("Cannot downshift to a gear lower than 1")
        else:
            self.gearbox.downshift()

    def shift(self):
        if self.car.gear=="R":
            self.gearbox.current_gear=-1
        if self.car.gear=="P" or self.car.gear=="N":
            self.gearbox.current_gear=0
        if self.car.gear=="D":
            self.gearbox.current_gear=1

