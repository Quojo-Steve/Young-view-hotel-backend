from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.TextField(max_length=100, primary_key=True, unique=True)
    capacity = models.IntegerField()
    sizes = (
        ('Executive', 'Executive'),
        ('Ordinary', 'Ordinary'),
        ('Standard', 'Standard'),
        )
    grade = models.CharField(max_length=100, choices=sizes)
    price = models.IntegerField()
    availability = models.BooleanField(default=True)
    next_booked_date = models.DateField(null=True)
    next_free_date = models.DateField(null=True)
    
    def __str__(self):
        return self.name
    
    
class Booking(models.Model):
    room_name = models.ForeignKey(Room, on_delete= models.SET_NULL, null=True)
    booking_id = models.CharField(max_length= 20, primary_key=True)
    guest_name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    arrival = models.DateField(null=True)
    departure = models.DateField(null=True)
    phone_number = models.CharField(max_length=10)
    idtypes=(
        ('Ghana Card', 'Ghana Card'),
        ('Driver\'s License', 'Driver\'s License'),
        ('Votter\'s Id', 'Votter\'s Id'),
    )
    id_type = models.CharField(max_length=20, choices=idtypes)
    id_number = models.CharField(max_length=30)
    amount_paid = models.FloatField()
    price = models.FloatField()
    
    def __str__(self):
        return self.room_name.name +" has been booked by " +self.guest_name