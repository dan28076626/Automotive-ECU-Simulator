class TCM:
    def __init__(self , car, gearbox, canbus):
        self.car=car
        self.gearbox=gearbox
        self.canbus=canbus

    def getcanbus(self):
        for message in self.canbus.get_messages("TCM"):
            if message["command"]=="CHANGE_GEAR":
                self.shift(message["data"])
                message["processed"]=True





            
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

    def shift(self, selector):
        if selector=="R":
            self.gearbox.current_gear=-1
        if selector=="P" or selector=="N":
            self.gearbox.current_gear=0
        if selector=="D":
            self.gearbox.current_gear=1
        print(self.gearbox.current_gear)
