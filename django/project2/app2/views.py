from django.shortcuts import render

from django.http import HttpResponse
def function1(req):
    return HttpResponse("hello app2")
def function2(req):
    return render(req,'app2/app2.html')