from django.db import models

# Create your models here.

class Information(models.Model):
    Care_Line = models.CharField(max_length=200)
    Address = models.TextField()
    Phone = models.CharField(max_length=200)
    Email = models.EmailField(max_length=100)
    Copyright = models.CharField(max_length=100)
    Designed = models.TextField()
    touch = models.TextField()
    Help_center = models.CharField(max_length=200)
    
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
    

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    feedback = models.TextField()
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    