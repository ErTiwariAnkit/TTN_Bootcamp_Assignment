from django.shortcuts import render

def home_page_set(req):
    return render(req,'home.html')
