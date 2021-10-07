import unittest
import quest4
class vehicletest(unittest.TestCase):
    def test1(self):
        a=23
        b=6
        c=10
        d=52
        car=quest4.Car("maruti",a,b)
        bus=quest4.Bus("bus",c,d)
        result=bus.get_fare()
        result1=car.get_fare()
        self.assertEqual(result1,158.7)
        self.assertEqual(result,650)
if __name__=="__main__":
    unittest.main()