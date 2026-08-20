class gearbox():
    # 0 is neutral/park | -1 is reverse | 1-7 are forward gears
    def __init__(self):
        self.current_gear=1
        self.gear_ratio={
            1: 3.909,
            2: 2.438,
            3: 1.810,
            4: 1.458,
            5: 1.185,
            6: 0.967,
            7: 0.844
        }
        self.reverse_ratio=2.929
        self.rear_final=2.867
        self.front_final=3.273

    def upshift(self):
        self.current_gear+=1

    def downshift(self):
        self.current_gear-=1