class Vehicle:

    def __init__(self,no_of_wheels):
        self.current_speed=0
        self.no_of_wheels = no_of_wheels
    def start(self):
        print("start vehicle")
    def stop(self):
        print("stop vehicle")
    def accelerate(self):
        self.current_speed=self.current_speed+10
    def Break(self):
        self.current_speed=self.current_speed-10
car=Vehicle(4)
print(car.no_of_wheels)
bike=Vehicle(2)
print(bike.no_of_wheels)
