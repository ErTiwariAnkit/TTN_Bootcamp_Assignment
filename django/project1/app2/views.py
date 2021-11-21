from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def function1(req):
    return HttpResponse("<h1>function1 app2</h1>")
def function2(req):
    return HttpResponse("function2 app2")
def template(req):
    return render(req,'app2.html')