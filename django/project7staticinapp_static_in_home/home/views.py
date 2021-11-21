from django.shortcuts import render

def set_home_page(req):
    return render(req,'home/home.html')