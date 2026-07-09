from car import Car
from ecu import ECU
from canbus import CANBus
my_car = Car()
bus = CANBus()
my_ecu = ECU("ABC123", my_car,bus)


print("Automotive ECU Simulator Started")
from canbus import CANBus



bus.send_message("Driver", "ECU", "UNLOCK_CAR", "NONE")
bus.send_message("Driver", "ECU", "REFUEL", 100)
bus.send_message("Driver", "ECU", "START_ENGINE", "NONE")
bus.send_message("Driver", "ECU", "SELECT_GEAR", "D")
bus.send_message("Driver", "ECU", "DRIVE_MILES", 5)
bus.send_message("Driver", "ECU", "SELECT_GEAR", "P")
bus.send_message("Driver", "ECU", "STOP_ENGINE", "NONE")
bus.send_message("Driver", "ECU", "LOCK_CAR", "NONE")
my_ecu.get_canbus()