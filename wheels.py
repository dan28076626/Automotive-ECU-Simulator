class Wheel:
    def __init__(self):
        self.tyre_width = 355          # mm
        self.aspect_ratio = 25         # %
        self.rim_diameter = 21         # inches

        self.sidewall_height = self.tyre_width * (self.aspect_ratio / 100)
        self.total_diameter = (self.rim_diameter * 25.4) + (2 * self.sidewall_height)

        self.circumference = (self.total_diameter * 3.14159) / 1000
        self.rpm = 0

    def calculate_wheel_rpm(self,speed_mph):

        # --- Convert mph to m/h ---
        speed_mh=speed_mph*1609.344

        # --- convert m/h to meters per minute ---
        speed_mm=speed_mh/60

        # --- Divide by wheen circumference to find wheel rpm ---
        wheel_rpm=speed_mm/self.circumference

        # --- Save values ---
        self.rpm=wheel_rpm

