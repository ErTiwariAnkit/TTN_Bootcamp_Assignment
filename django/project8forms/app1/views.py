from django.http import request
from django.shortcuts import render
from .forms import studentreg
def studentregis(req):
    stud=studentreg()
    return render(req,'app1/app1.html',{'student':stud})
def showformdata(req):
    if req.method == 'POST':
        stud1=studentreg(req.POST)
        if stud1.is_valid():
            print('form valid')
            print(stud1.cleaned_data['name'])
            print(stud1.cleaned_data['email'])
            print(stud1.cleaned_data['age'])
    else:
        stud1=studentreg()
    return render(req,'app1/app1.html',{'student':stud1})