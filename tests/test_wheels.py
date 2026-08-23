import pytest
from wheels import Wheel

@pytest.fixture
def wheel():
    return Wheel()

def test_calculate_rpm(wheel):
    wheel.calculate_rpm(60)

    assert wheel.rpm==pytest.approx(720.6, abs=0.1)