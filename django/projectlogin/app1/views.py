from django.shortcuts import render,redirect

def function1(req):
    if not req.user.is_authenticated:
        return redirect('mylogin')
    return render(req,'app1.html')