from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == "GET":
            return render(request,'register.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists() :
            return render(request,'register.html',{'status':"EMAIL ALREADY EXISTS"})    
        elif User.objects.filter(username=username).exists():
            return render(request,'register.html',{'status':"USERNAME ALREADY EXISTS"})    

        else:    
            user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)

        user.save()
        print("user created")

        return redirect("/")