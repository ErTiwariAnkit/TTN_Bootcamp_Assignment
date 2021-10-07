import unittest
import quest6
class Pointadd(unittest.TestCase):
    def test1(self):
        p1=quest6.Point(3,4)
        p2=quest6.Point(2,6)
        result=p1+p2
        self.assertEqual(result,(5,10))
if __name__=="__main__":
    unittest.main()