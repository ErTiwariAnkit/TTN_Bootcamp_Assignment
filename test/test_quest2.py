import unittest
import quest2_sum
class Sumtest(unittest.TestCase):
    def test_sum(self):
        num=123
        res=quest2_sum.sum_fun(num)
        self.assertEqual(res,6)
if __name__=="__main__":
    unittest.main()