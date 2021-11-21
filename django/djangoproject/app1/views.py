from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def django_function(request):
    return HttpResponse("hello world")