from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        us = str(user)
        if user is not None:
            auth.login(request,user)
            return HttpResponse("Hello "+us+"!!! You have successfully logged in!")
        else:
            return render(request,'login.html',{'status':"Incorrect Email or Password!"}) 


def forgetpass(request):
    return HttpResponse("FORGET PASS PAGE!")
    