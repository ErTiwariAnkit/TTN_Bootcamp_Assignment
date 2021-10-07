import unittest
import quest1
class Employeetest(unittest.TestCase):
    def test1(self):
        emp1 = quest1.Emoloyee("anand", "tiwari", 40000)
        result=emp1.email_id
        self.assertEqual(result,"anand.tiwari@tothenew.com")
if __name__=="__main__":
    if __name__ == '__main__':
        unittest.main()
