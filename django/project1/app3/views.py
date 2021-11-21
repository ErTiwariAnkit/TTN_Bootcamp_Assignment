from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld(request):
    return HttpResponse("hello world")
def function1(req):
    return HttpResponse("<h1>function1 app3</h1>")
def function2(req):
    return HttpResponse("function2 app3")
def template(req):
    return render(req,'app3.html')