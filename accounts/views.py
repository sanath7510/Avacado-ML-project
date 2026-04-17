
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    if request.method=="POST":
        user=authenticate(request,
            username=request.POST.get("username"),
            password=request.POST.get("password"))
        if user:
            login(request,user)
            return redirect("/predict/")
    return render(request,"accounts/login.html")

def register_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username,email=email,password=password)
            return redirect("/login/")
    return render(request,"accounts/register.html")

def logout_view(request):
    logout(request)
    return redirect("/login/")
