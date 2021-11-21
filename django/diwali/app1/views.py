from django.shortcuts import render

def function1(req):
    return render(req,'app1.html')
def error_404_error(req,exception):
    return render(req,'404.html')