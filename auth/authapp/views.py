from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm

# Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# This is for homepage:

def homepage(request):
    return render(request, 'authapp/index.html')


# This is for register:

def register(request):
    
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my_login")
    
    context = {'registerform':form}
    
    return render(request, 'authapp/register.html', context=context)



# This is for login:

def my_login(request):
    
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
       
    context = {'loginform':form}
            
    return render(request, 'authapp/my-login.html', context=context)


# This is for user logout:

def user_logout(request):
    
    auth.logout(request)
    return redirect("")


# This is for dashboard

@login_required(login_url="my_login")
def dashboard(request):
    return render(request, 'authapp/dashboard.html')