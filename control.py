from car import Car
from modules.ecu import ECU
from modules.canbus import CANBus
from modules.dashboard import Dashboard
my_car = Car()
bus = CANBus()
my_ecu = ECU("ABC123", my_car,bus)
dashboard=Dashboard(bus)
import sys as s


print("Automotive ECU Simulator Started")
print("Options: \n 1. Unlock doors \n 2. Lock doors \n 3. Start engine \n 4. Stop engine \n 5. Reufel \n 6.Drive \n 7. Select gear \n 8.Exit")
while True:
  
    opt=input("Choose an option (number)")

    if opt=="1":
        keyfobsignal=input("Enter keyfobsignal: ")
        bus.send_message("DRIVER", "ECU", "UNLOCK_CAR", keyfobsignal)
    elif opt=="2":
        bus.send_message("Driver", "ECU", "LOCK_CAR", "NONE")
    elif opt=="3":
        bus.send_message("Driver", "ECU", "START_ENGINE", "NONE")
    elif opt=="4":
        bus.send_message("Driver", "ECU", "STOP_ENGINE", "NONE")
    elif opt=="5":
        amount=int(input("Enter amount to refuel"))
        bus.send_message("Driver", "ECU", "REFUEL", amount)
    elif opt=="6":
        miles=int(input("How many miles do you want to drive"))
        bus.send_message("Driver", "ECU", "DRIVE_MILES", miles)
    elif opt=="7":
        gear=input("What gear do you want to use? ")
        bus.send_message("Driver", "ECU", "SELECT_GEAR", gear)
    elif opt=="8":
        target_speed=int(input("What speed do you want to travel at"))
        bus.send_message("Driver", "ECU", "ACCELERATE", target_speed)
    elif opt=="9":
        print("Exiting simulator")
        s.exit()
    my_ecu.get_canbus()
    dashboard.getcanbus()
    dashboard.display_dashboard()
    