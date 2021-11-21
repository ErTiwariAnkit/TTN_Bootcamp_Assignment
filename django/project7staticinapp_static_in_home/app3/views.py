from django.shortcuts import render

def function1(req):
    return render(req,'app3.html',{'home':'Home django page'})