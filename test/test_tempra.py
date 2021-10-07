import unittest
import temperature
class temprature(unittest.TestCase):
    def test3(self):
        result=temperature.convert_cel_to_far(37)
        result1=temperature.convert_far_to_cel(72)
        self.assertEqual(result,98.60)
        self.assertEqual(result1,22.22)
if __name__=="__main__":
    unittest.main()