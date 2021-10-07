class Emoloyee:
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
        self.email_id=f"{first_name}.{last_name}@tothenew.com"
emp1=Emoloyee("anand","tiwari",40000)
print(emp1.first_name)
print(emp1.last_name)
print(emp1.salary)
print(emp1.email_id)