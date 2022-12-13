from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from receptionist.models import Collective_Room

# Create your views here.
def index(request):
    rooms = Collective_Room.objects.all()
    return render(request, 'user_main.html', {'rooms':rooms})

def login(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = fname+' '+lname
        password = request.POST['pswd']
        # email2 = request.POST['email2']
        # password2 = request.POST['pswd2']
        
        if User.objects.filter(username = username).exists():
            messages.info(request, 'Username taken')
            return redirect('/login')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'Email taken')
            return redirect('/login')
        else:
            User.objects.create_user(username= username, password= password, email=email, last_name= lname, first_name= fname)
            User.save
            messages.info(request, 'Now login please')
            return redirect('/login')
        
        if request.method == 'POST':
            email2 = request.POST['email2']
            password2 = request.POST['pswd2']
            
            if User.objects.filter(email=email2).exists():
                logger = User.objects.filter(email=email2).first()
                username2 = logger.username
                user = auth.authenticate(username = username2, password = password)
        
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    messages.info(request, 'Invalid Credentials')
                    return redirect('/login')
            
    return render(request, 'user_login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/login')