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
    appointment = models.TextField(null= True , blank=True)
    time = models.TextField(null= True , blank=True)
    fee = models.DecimalField(max_digits=10 , decimal_places= 2 , null= True , blank=True)
    image = models.ImageField(upload_to = "image/" , null= True , blank=True)
    
    def __str__(self):
        return self.name
    

class Room(models.Model):
    room_type = models.CharField(max_length=100)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.room_type
    

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    feedback = models.TextField()
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
 
class Appointment(models.Model):
    doctor_name = models.CharField(max_length= 100 , null = True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.doctor_name    