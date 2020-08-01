from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'Login.html')
    else:
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponse("Hello"+user+"!!! You have successfully logged in!")
        else:
            return render(request,'Login.html',{'status':"Incorrect Email or Password!"}) 