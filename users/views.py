from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from receptionist.models import Collective_Room, Room, Booking
from receptionist.views import daterange
from datetime import datetime

# Create your views here.
def index(request):
    rooms = Collective_Room.objects.all()
    return render(request, 'user_main.html', {'rooms':rooms})

def login(request):        
    if request.method == 'POST':
        email2 = request.POST['email2']
        password2 = request.POST['pswd2']
        
        if User.objects.filter(email=email2).exists():
            logger = User.objects.filter(email=email2).first()
            username2 = logger.username
            user = auth.authenticate(username = username2, password = password2)
    
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

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = fname+' '+lname
        password = request.POST['pswd']
        password2 = request.POST['pswd2']
        if password != password2:
            messages.info(request, 'Passwords don\'t match')
            return redirect('/signup')
        elif User.objects.filter(username = username).exists():
            messages.info(request, 'Username taken')
            return redirect('/signup')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'Email taken')
            return redirect('/signup')
        else:
            User.objects.create_user(username= username, password= password, email=email, last_name= lname, first_name= fname)
            User.save
            messages.info(request, 'Now login please')
            return redirect('/login')
    return render(request, 'user_signup.html')

def booking(request, pk):
    if pk == 'Ordinary':
        return redirect('/ordinary')
    if pk == 'Executive':
        return redirect('/executive')
    if pk == 'Standard':
        return redirect('/standard')
    return render(request, 'user_book_room.html')

def standardRoomBooking(request):
    
    rooms = Room.objects.filter(grade='Standard')
    print(rooms)
    return render(request, 'user_book_room_stan.html')

def ordinaryRoomBooking(request):
    rooms = Room.objects.filter(grade='Ordinary')
    books = Booking.objects.filter(expired=False)
    if request.method == 'POST':
        arrival = request.POST['arrival']
        departure = request.POST['dep']
        guest = request.POST['guest']
        number = request.POST['num']
        price = request.POST['price']
        
        chosen = []
        # for room in rooms:
        #     books = Booking.objects.filter(room_name=room.grade)
        #     for book in books:
        #         dates = daterange(book.arrival, book.departure)
        #         new_dates = daterange(arrival, departure)
                
        #         for datey in dates:
        #             for new_date in new_dates:
        #                 if new_date == datey:
        #                     break
        #                 else:
        #                     print('yah')
            
        for room in rooms:
            if room.name == 'K1':
                for book in books:
                    
                    if book.room_name.name == room.name:
                        chosen.append(book)    
            elif room.name == 'K2':
                for book in books:
                    
                    if book.room_name.name == room.name:
                        chosen.append(book)   
            elif room.name == 'K3':
                for book in books:
                    
                    if book.room_name.name == room.name:
                        chosen.append(book)   
            elif room.name == 'K4':
                for book in books:
                   
                    if book.room_name.name == room.name:
                        chosen.append(book)   
            elif room.name == 'K5':
                for book in books:
                    
                    if book.room_name.name == room.name:
                        chosen.append(book)   
        
        for chose in chosen:
            dates = daterange(chose.arrival, chose.departure)
            # arrival_date = datetime.strptime(arrival, '%d/%m/%y')
            # departure_date = datetime.strptime(departure, '%d/%m/%y')
            print(arrival)
            print(departure)
            new_date = daterange(arrival, departure)
            print(new_date)      
        
                
    return render(request, 'user_book_room_ord.html')

def executiveRoomBooking(request):
    rooms = Room.objects.filter(grade='Executive')
    print(rooms)
    return render(request, 'user_book_room_exec.html')