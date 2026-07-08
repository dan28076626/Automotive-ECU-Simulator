from car import Car
from ecu import ECU
 
my_car = Car()
my_ecu = ECU("ABC123", my_car)

print("Automotive ECU Simulator Started")
my_ecu.unlock_car("ABC123")
my_ecu.start_engine()
my_car.display_dashboard()
my_ecu.select_gear("D")
my_ecu.drive_miles(3)
