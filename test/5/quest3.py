class Emoloyee:
    raise_percentage = 10
    def raise_percentage1(self,num):
        Emoloyee.raise_percentage=Emoloyee.raise_percentage+num
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
        self.email_id=f"{first_name}.{last_name}@tothenew.com"
    def raise_salary(self):
        self.salary=self.salary+(self.salary*Emoloyee.raise_percentage/100)

emp1=Emoloyee("anand","tiwari",40000)
#print(emp1.first_name)
#print(emp1.last_name)
#print(emp1.salary)
#print(emp1.email_id)
#emp1.raise_salary()
#print(emp1.salary)
#emp1.raise_percentage1(5)
emp1.raise_salary()
print(emp1.salary)