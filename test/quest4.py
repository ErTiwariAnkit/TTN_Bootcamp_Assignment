class Vehicle:
    def __init__(self,make,mileage,capacity):
        self.make=make
        self.mileage=mileage
        self.capacity=capacity
    def get_fare(self):
        pass
class Car(Vehicle):
    def __init__(self,make,mileage,capacity):
        Vehicle.__init__(self,make,mileage,capacity)
    def get_fare(self):
        fare=(self.mileage*self.capacity)
        fare=fare+(fare*15/100)
        return fare
class Bus(Vehicle):
    def __init__(self,make,mileage,capacity):
        Vehicle.__init__(self,make,mileage,capacity)
    def get_fare(self):
        fare=(self.mileage*self.capacity)
        fare=fare+(fare*25/100)
        return fare