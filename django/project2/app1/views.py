from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def function1(req):
    return HttpResponse("hello app1")
def function2(req):
    date=datetime.now()
    dict1={'name':'ankit tiwari'}
    date1={'date':date}
    return render(req,'app1/app1.html',dict1)
