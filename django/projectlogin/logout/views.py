from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
def logout_page(req):
    logout(req)
    return redirect('mylogin')