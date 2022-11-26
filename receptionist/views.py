from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Room

# Create your views here.

def index(request):
    return render(request, 'index.html')

def emp_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('./emp_dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('./emp_login')
                
    return render(request, 'emp_login.html')


    return render(request, "emp_change_password.html")

def emp_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if User.objects.filter(first_name = otp).exists():
            fake = User.objects.filter(first_name = otp)
            fake.delete()
            return redirect('./emp_register')
        else:
            messages.info(request, 'No such OTP')
            return redirect('./emp_otp')
    return render(request, 'emp_otp.html')

def emp_register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username taken')
                return redirect('./emp_register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email taken')
                return redirect('./emp_register')
            else:
                User.objects.create_user(username= username, password= password, email=email, last_name= lname, first_name= fname)
                User.save
                return redirect('./emp_login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('./emp_register')
                
    return render(request, 'emp_register.html')

@login_required(login_url = './emp_login')
def emp_dashboard(request):
    return render(request, 'emp_dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('./')

@login_required(login_url = './emp_login')
def emp_rooms(request):
    all_rooms = Room.objects.all()
    return render(request, 'emp_rooms.html', {'all_rooms': all_rooms})

def emp_room(request, pk):
    room = Room.objects.get(id = pk)
    print(room)
    return render(request, 'emp_room.html', {'room': room})
    