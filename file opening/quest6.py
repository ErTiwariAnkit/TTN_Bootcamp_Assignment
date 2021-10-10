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
        f.close()
    def file_read(self):
        f=open("stuent.txt","r")
        data=f.readlines()
        print(data)
        f.close()
student1=Student("Anurag",100,"math")
student2=Student("Arpit",101,"Hindi")
student3=Student("Anand",102,"Science")
student4=Student("Anurag",103,"math")
student5=Student("Anurag",104,"math")
student6=Student("Anurag",105,"math")
student7=Student("Anurag",106,"math")
student1.file_save()
student2.file_save()
student3.file_save()
student4.file_save()
student5.file_save()
student6.file_save()
student7.file_save()
def replace_text(file_path,search_term,new_term,replace_all):
    f=open(file_path,"r+")
    data=f.read()
    if replace_all==True:
        data=data.replace(search_term,new_term)
    else:
        data=data.replace(search_term,new_term,1)
    search_term=new_term
    coun = data.count(search_term)
    print(coun)
    f.write(data)
    f.close()
f=open("stuent.txt","r")
replace_text("/home/ankit/bootcamp assign/TTN_Bootcamp_Assignment/file opening/stuent.txt",
             "Anurag","shahsank",False)
print(f.read())
f.close()

