from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length= 200)
    speciality = models.TextField()
    degree = models.TextField()
    intro = models.TextField()
    complete = models.TextField()
    end = models.TextField()
    

class Room(models.Model):
    room_type = models.CharField(max_length=100)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    
    
