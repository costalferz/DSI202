from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Customer,Job,Designer
from django.views.generic.list import ListView
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'index.html')
def service(request):
    return render(request,'service.html')
def learning_center(request):
    return render(request,'knowledge.html')
def about(request):
    return render(request,'about.html')
def loginForm(request):
    return render(request,'login.html')
def sign_up(request):
    return render(request,'sign_up.html')
def success(request):
    return render(request,'success.html')
def addUser(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']
    age=request.POST['age']
    phone_num=request.POST['phone_num']
    email=request.POST['email']
    career=request.POST['career']
    business_size=request.POST['business_size']
    interest=request.POST['interest']
    message=request.POST['message']
    if password==repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,"This User id has already been registered.")
            return redirect('/sign_up')
        elif  User.objects.filter(email=email).exists():
            messages.info(request,"This email has already been registered.")
            return redirect('/sign_up')
        else:
            new_user= User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname
            )
            customer=Customer.objects.create(
            user=new_user,
            phone_num=phone_num,
            age=age,
            career=career,
            business_size=business_size,
            interest=interest,
            message=message
            )
            new_user.save()
            customer.save()
            return redirect('/')
    else:
        messages.info(request,"password doesn't match")
        return redirect('/sign_up')
def login(request):
    username=request.POST['username']
    password=request.POST['password']
     #login
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,"Data not found please Try again")
        return redirect('/loginForm')
def logout(request):
    auth.logout(request)
    return redirect('/')
def buy(request):
        current_user=request.user
        package=request.POST['package']
        if package=='Package A':
                cost=999
        elif package=='Package B':
                cost=1299
        elif package=='Package C':
                cost=4599
        elif package=='Application Package':
                cost=7999
        customer_tell=request.POST['customer_tell']
        Job.objects.create(
            customer=Customer.objects.get(user=current_user),
            package=package,
            cost=cost,
            customer_tell=customer_tell
        )
        return redirect('/success')
def please(request):
    return redirect('/loginForm')
        