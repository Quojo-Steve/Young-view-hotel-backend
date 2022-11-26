from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.TextField(max_length=100)
    capacity = models.IntegerField()
    sizes = (
        ('Executive', 'Executive'),
        ('Ordinary', 'Ordinary'),
        ('Standard', 'Standard'),
        )
    grade = models.CharField(max_length=100, choices=sizes)
    price = models.IntegerField()
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name