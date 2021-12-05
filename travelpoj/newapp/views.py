from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        passw=request.POST['password']
        user=auth.authenticate(username=uname,password=passw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        un=request.POST['username']
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        em=request.POST['email']
        ps1=request.POST['password1']
        ps2=request.POST['password2']

        if ps1==ps2:
            if User.objects.filter(username=un).exists():
                messages.info(request,'username exists')
                return redirect('register')

            elif User.objects.filter(email=em).exists():
                messages.info(request,'email exists')
                return redirect('register')

            else:
                user=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=ps1)
                user.save();
                return redirect('login')
                # return redirect('/')

        else:
            messages.info(request,'password not matching')
            return redirect('register')
        # return redirect('/')
    else:
        return render(request,'register.html')

def logout(requst):
    auth.logout(requst)
    return redirect('/')