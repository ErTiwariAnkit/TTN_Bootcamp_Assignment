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
        fare=(self.mileage*self.capacity)+15/100
        return fare
class Bus(Vehicle):
    def __init__(self,make,mileage,capacity):
        Vehicle.__init__(self,make,mileage,capacity)
    def get_fare(self):
        fare=(self.mileage*self.capacity)+25/100
        return fare
car=Car("maruti",23,6)
bus=Bus("bus company",10,52)
print(bus.make)
print(bus.mileage)
print(bus.capacity)
print("bus fare ",bus.get_fare())
print(car.make)
print(car.mileage)
print(car.capacity)
print("car fare",car.get_fare())