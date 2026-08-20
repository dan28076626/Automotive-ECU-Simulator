from car import Car

class Test_car():

    def test_acceleration(self):
        car=Car()
        # --- Save Values ---
        starting_fuel=car.fuel

        # --- Accelerate ---
        car.accelerate(60)

        # --- Check Results ---
        assert car.speed ==60
        assert car.odometer>0
        assert car.fuel<starting_fuel

    def test_braking(self):
        car=Car()

        # --- Accelerate ---
        car.accelerate(60)

        # --- Save values ---
        odometer_before=car.odometer

        # --- Brake ---
        car.braking(100,0)

        # --- Check Results ---
        assert car.speed == 0
        assert odometer_before <car.odometer