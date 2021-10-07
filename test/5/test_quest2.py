import unittest
import quest2
class Employeetest1(unittest.TestCase):
    def test1(self):
        emp1 = quest2.Emoloyee("anand", "tiwari", 40000)
        emp1.raise_salary()
        result=emp1.salary
        self.assertEqual(result,44000)
if __name__=="__main__":
    unittest.main()