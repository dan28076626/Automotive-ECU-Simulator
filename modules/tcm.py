class TCM:
    def __init__(self , car, gearbox, canbus,wheel):
        self.car=car
        self.gearbox=gearbox
        self.canbus=canbus
        self.wheel=wheel


    def getcanbus(self):
        for message in self.canbus.get_messages("TCM"):
            if message["command"] == "CHANGE_GEAR":
                self.shift(message["data"])
            elif message["command"] == "UPSHIFT":
                self.upshift()
            elif message["command"] == "DOWNSHIFT":
                self.downshift()
            elif message["command"] == "CHANGE_RPM":
                self.calculate_engine_rpm(message["data"])

            message["processed"] = True

    def update_dashboard(self):
        self.canbus.send_message("TCM", "DASHBOARD", "UPDATE_RPM", self.car.rpm)
        self.canbus.send_message("TCM", "DASHBOARD", "UPDATE_GEAR", self.gearbox.current_gear)



            
    def upshift(self):
        if self.gearbox.current_gear==7:
            print("Cannot upshift to a gear higher than 7")
        else:
            self.gearbox.upshift()
            self.calculate_engine_rpm(self.car.speed)
            self.update_dashboard()

    def downshift(self):
        if self.gearbox.current_gear == 1:
            print("Cannot downshift to a gear lower than 1")

        else:
            simulated_rpm = self.simulate_engine_rpm()

            if simulated_rpm > self.car.max_rpm:
                print("Cannot downshift: RPM would be too high")

            else:
                self.gearbox.downshift()
                self.calculate_engine_rpm(self.car.speed)
                self.update_dashboard()

    def shift(self, selector):
        if selector=="R":
            self.gearbox.current_gear=-1
            self.update_dashboard()
        if selector=="P" or selector=="N":
            self.gearbox.current_gear=0
            self.update_dashboard()
        if selector=="D":
            self.gearbox.current_gear=1
            self.update_dashboard()
        print(self.gearbox.current_gear)

    def calculate_engine_rpm(self, speed):
        self.wheel.calculate_wheel_rpm(speed)

        engine_rpm=self.wheel.rpm*self.gearbox.rear_final*self.gearbox.gear_ratio[self.gearbox.current_gear]

        self.car.rpm=engine_rpm
        self.update_dashboard()

    def simulate_engine_rpm(self):
        self.wheel.calculate_wheel_rpm(self.car.speed)
        gear=self.gearbox.current_gear-1

        engine_rpm=self.wheel.rpm*self.gearbox.rear_final*self.gearbox.gear_ratio[gear]

        return engine_rpm
        
