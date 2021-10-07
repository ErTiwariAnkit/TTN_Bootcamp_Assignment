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
student1=Student("Anurag",100,"math")
student2=Student("Arpit",101,"Hindi")
student3=Student("Anand",102,"Science")
student1.file_save()
student2.file_save()
student3.file_save()
def file_read():
    f = open("stuent.txt", "r")
    data = f.readlines()
    print(data)
def gen_funct():
    f = open("stuent.txt", "r")
    for i in f.readlines():
        yield i
file_read()
it=gen_funct()
print(next(it))
print(next(it))
print(next(it))

