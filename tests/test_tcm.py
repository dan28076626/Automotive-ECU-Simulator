import pytest
from modules.tcm import TCM
from gearbox import Gearbox
from car import Car
from wheels import Wheel
from modules.canbus import CANBus


@pytest.fixture
def tcm():
    car = Car()
    gearbox = Gearbox()
    wheel = Wheel()
    canbus = CANBus()

    return TCM(car, gearbox, canbus, wheel)

def test_engine_rpm(tcm):
    # --- Set gear ---
    tcm.gearbox.current_gear = 3

    # --- Calculate rpm ---
    tcm.calculate_engine_rpm(60)

    # --- Check results
    assert tcm.car.rpm == pytest.approx(3739.36, abs=0.1)

def test_upshift(tcm):
    # --- Set gear and speed ---
    tcm.gearbox.current_gear=3
    tcm.car.speed=60

    # --- Calculate rpm ---
    tcm.calculate_engine_rpm(tcm.car.speed)

    # --- Save RPM ---
    rpm=tcm.car.rpm

    # --- Upshift ---
    tcm.upshift()

    # --- Check results ---
    assert tcm.car.speed==60
    assert tcm.car.rpm<rpm
    assert tcm.gearbox.current_gear==4
    

    
def test_safe_downshift(tcm):
    # --- Set gear and speed ---
    tcm.gearbox.current_gear=4
    tcm.car.speed=60

    # --- Calculate rpm ---
    tcm.calculate_engine_rpm(tcm.car.speed)

    # --- Save rpm ---
    rpm=tcm.car.rpm

    # --- Downshift ---
    tcm.downshift()

    # --- Check results ---
    assert tcm.car.speed==60
    assert tcm.car.rpm>rpm
    assert tcm.gearbox.current_gear==3


def test_unsafe_rpm(tcm):
    # --- Set gear and speed ---
    tcm.gearbox.current_gear=3
    tcm.car.speed=110

    # --- Downshift ---
    tcm.downshift()

    # --- Check results ---
    assert tcm.car.speed==110
    assert tcm.gearbox.current_gear==3

def test_upper_boundary(tcm):
    # --- Set gear ---
    tcm.gearbox.current_gear=7

    # --- Upshift ---
    tcm.upshift()

    # --- Check results ---
    assert tcm.gearbox.current_gear==7

def test_lower_boundary(tcm):
    # --- Set gear ---
    tcm.gearbox.current_gear=1

    # --- Downshift ---
    tcm.downshift()

    # --- Check results ---
    assert tcm.gearbox.current_gear==1
    