import pytest
from car import Car
@pytest.fixture
def car():
    return Car()

def test_accelerationc(car):
    
    # --- Save Values ---
    starting_fuel=car.fuel

    # --- Accelerate ---
    car.accelerate(60)

    # --- Check Results ---
    assert car.speed ==60
    assert car.odometer>0
    assert car.fuel<starting_fuel

def test_braking(car):


    # --- Accelerate ---
    car.accelerate(60)

    # --- Save values ---
    odometer_before=car.odometer

    # --- Brake ---
    car.braking(100,0)

    # --- Check Results ---
    assert car.speed == 0
    assert odometer_before <car.odometer

def test_deceleration(car):
  

    # --- Accelerate ---
    car.accelerate(60)

    # --- Save Values ---
    odometer=car.odometer
    fuel=car.fuel

    # --- Decelerate ---
    car.decelerate(30)

    # --- Check Results ---
    assert car.speed==30
    assert car.odometer>odometer
    assert car.fuel<fuel

def test_travel(car):

    # --- Set car speed ---
    car.speed=60

    # --- Save Values ---
    odometer=car.odometer
    fuel=car.fuel

    # --- Travel ---
    car.travel(30)

    # --- Check Results ---
    assert car.speed==60
    assert fuel>car.fuel
    assert odometer<car.odometer


def test_fuel_used(car):

    # --- Set fuel ---
    car.fuel=50

    # --- Save values ---
    fuel = car.fuel

    # --- Fuel Used ---
    actual_distance = car.fuel_used(10)

    # --- Check results
    assert car.fuel < fuel
    assert actual_distance == 10
     

def test_low_fuel(car):

    # --- Set fuel ---
    car.fuel=1

    # --- Fuel Used ---
    actual_distance=car.fuel_used(100)

    # --- Check results ---
    assert car.fuel==0
    assert actual_distance<100
    assert actual_distance > 0

    

def test_refuel(car):

    # --- Set fuel ---
    car.fuel=50

    # --- Refuel ---
    car.refuel(50)

    # --- Check results ---
    assert car.fuel==100


def test_refuel_overfill(car):

    # --- Set fuel ---
    car.fuel = 90

    # --- Refuel ---
    car.refuel(50)

    # --- Check results ---
    assert car.fuel == 100