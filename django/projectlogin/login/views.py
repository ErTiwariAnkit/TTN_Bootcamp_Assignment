from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
def login_page(request):
    if request.method=='POST':
        user=request.POST.get('u')
        upassword=request.POST.get('p')
        print(user,upassword)
        if user!="" and upassword!="":
            user=authenticate(username=user,password=upassword)
            if user!=None:
                login(request,user)
                print(user,upassword)
                return redirect('function1')
    return render(request,'login.html')