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
    tcm.gearbox.current_gear = 3
    tcm.calculate_engine_rpm(60)

    assert tcm.car.rpm == pytest.approx(3739.36, abs=0.1)
    

    

    

    