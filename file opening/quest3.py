class Student:
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course
    def file_save(self):
        f=open("stuent.txt",mode="a")
        f.write(f"{self.name} ")
        f.write(f"{self.roll_no} ")
        f.write(f"{self.course}\n")
    def file_read(self):
        f=open("stuent.txt","r")
        data=f.readlines()
        return data
student1=Student("Anurag",100,"math")
student2=Student("Arpit",101,"Hindi")
student3=Student("Anand",102,"Science")
student1.file_save()
student2.file_save()
student3.file_save()
print(student1.file_read())
