from modules.ecu import ECU
from modules.canbus import CANBus
from car import Car


class Dashboard():
    def __init__(self, car,canbus):
        self.car=car
        self.canbus=canbus

    def display_dashboard(self):
        print("\n--- DASHBOARD ---")
        print(f"Doors locked: {self.doors_locked}")
        print(f"Engine running: {self.engine_running}")
        print(f"Gear: {self.gear}")
        print(f"Fuel: {self.fuel}%")
        print(f"Odometer: {self.odometer} miles")
        print(f"Speed: {self.speed} mph")
        print(f"RPM: {self.rpm}")
        print("-----------------\n")