from django.shortcuts import render
from app1.models import student

def function1(req):
    stud=student.objects.get(pk=2)
    print(stud)
    return render(req,'app1.html',{'stu':stud})