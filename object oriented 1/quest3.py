class Vehicle:
    no_of_wheels=None
    def __init__(self,current_speed):
        self.current_speed=0
    def start(self):
        print("start vehicle")
    def stop(self):
        print("stop vehicle")
    def accelerate(self):
        self.current_speed=self.current_speed+10
    def Break(self):
        self.current_speed=self.current_speed-10
car=Vehicle(0)
bike=Vehicle(0)
