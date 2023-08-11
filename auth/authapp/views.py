from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, 'authapp/index.html')

def register(request):
    return render(request, 'authapp/register.html')

def my_login(request):
    return render(request, 'authapp/my-login.html')

def dashboard(request):
    return render(request, 'authapp/dashboard.html')