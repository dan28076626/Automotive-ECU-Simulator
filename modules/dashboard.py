
class Dashboard():
    def __init__(self,canbus):
        self.canbus=canbus

        self.rpm=0
        self.gear="0"
        self.fuel=0
        self.odometer=0
        self.speed=0
        self.doors_locked=False
        self.engine_running=False
        self.gear_selector="P"


    def getcanbus(self):
        for message in self.canbus.get_messages("DASHBOARD"):
            if message["id"] == "0x102" and not message["processed"]:

                if message["command"] == "UPDATE_RPM":  
                    self.rpm = message["data"]
                    print("Recieved")

                elif message["command"] == "UPDATE_FUEL":
                    self.fuel = message["data"]

                elif message["command"] == "UPDATE_GEAR_SELECTOR":
                    self.gear_selector = message["data"]

                elif message["command"] == "UPDATE_SPEED":
                    self.speed = message["data"]

                elif message["command"] == "UPDATE_ODOMETER":
                    self.odometer = message["data"]

                elif message["command"] == "UPDATE_ENGINE":
                    self.engine_running = message["data"]

                elif message["command"] == "UPDATE_DOORS":
                    self.doors_locked = message["data"]

                elif message["command"]=="UPDATE_GEAR":
                    self.gear=message["data"]

                message["processed"] = True

    def display_dashboard(self):
        print("\n--- DASHBOARD ---")
        print(f"Doors locked: {self.doors_locked}")
        print(f"Engine running: {self.engine_running}")
        print(f"Gear Selector: {self.gear_selector} ")
        print(f"Gear: {self.gear}")
        print(f"Fuel: {self.fuel:.2f}%")
        print(f"Odometer: {self.odometer:.2f} miles")
        print(f"Speed: {self.speed} mph")
        print(f"RPM: {self.rpm}")
        print("-----------------\n")


