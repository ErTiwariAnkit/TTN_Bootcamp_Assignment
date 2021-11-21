from django.shortcuts import render

def function1(req):
    dict2={'company':'TTN'}
    return render(req,'app1/app1.html',dict2)
