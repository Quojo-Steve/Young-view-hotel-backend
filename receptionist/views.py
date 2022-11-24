from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth

# Create your views here.

def index(request):
    return render(request, 'index.html')

def emp_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            return redirect('emp_change_password')
        else:
            return redirect('')
                
    return render(request, 'emp_login.html')

def empchangepassword(request):
    return render(request, "emp_change_password.html")