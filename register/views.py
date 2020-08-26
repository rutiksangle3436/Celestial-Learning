from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from Celestial_Learning.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.

def register(request):

    if request.method == "GET":
            return render(request,'register.html')
    else:
        #first_name = request.POST['first_name']
        #last_name = request.POST['last_name']
        username = request.POST['email']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists() :
            return render(request,'index.html',{'status':"EMAIL ALREADY EXISTS"})    
        elif User.objects.filter(username=username).exists():
            return render(request,'register.html',{'status':"USERNAME ALREADY EXISTS"})    

        else:    
            user = User.objects.create_user(username=username,email=email,password=password)
            subject = 'Welcome to Celestial Learning'
            message = 'Hello ' + name + '! \nWelcome to Celestial Learning! Enjoy your new journey of learning!!' 
            recepient = str(email)
            send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return HttpResponse("You have successfully registered!")



        user.save()

        return redirect("/")