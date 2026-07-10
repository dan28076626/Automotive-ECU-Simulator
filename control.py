from car import Car
from modules.ecu import ECU
from modules.canbus import CANBus
from modules.dashboard import Dashboard
my_car = Car()
bus = CANBus()
my_ecu = ECU("ABC123", my_car,bus)
dashboard=Dashboard(bus)


print("Automotive ECU Simulator Started")




bus.send_message("DRIVER", "ECU")
my_ecu.get_canbus()