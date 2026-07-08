from car import Car
from ecu import ECU
from canbus import CANBus
my_car = Car()
my_ecu = ECU("ABC123", my_car)
bus = CANBus()

print("Automotive ECU Simulator Started")
from canbus import CANBus



bus.send_message("Driver", "ECU", "START_ENGINE")
bus.send_message("Driver", "ECU", "SELECT_GEAR_D")
bus.send_message("Driver", "ECU", "DRIVE_1_MILE")