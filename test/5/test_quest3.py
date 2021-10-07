import unittest
import quest3
class Employee(unittest.TestCase):
    def test1(self):
        emp1 = quest3.Emoloyee("anand", "tiwari", 40000)
        emp1.raise_percentage1(5)
        emp1.raise_salary()
        result=emp1.salary
        print(result)
        self.assertEqual(result,46000)
if __name__=="__main__":
    unittest.main()