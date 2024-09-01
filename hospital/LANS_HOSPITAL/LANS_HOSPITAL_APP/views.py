from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello, world')

def home(request):
    return render(request, "index.html")

def media(request):
    return render(request ,"media.html")

def brain(request):
    return render(request ,"brain.html")
def bone(request):
    return render(request ,"bone.html")
def gastro(request):
    return render(request ,"gastro.html")
def mother(request):
    return render(request ,"mother.html")
def nephrologycenter(request):
    return render(request ,"nephrologycenter.html")
def anesthesia(request):
    return render(request ,"anesthesia.html")
def urology(request):
    return render(request ,"urology.html")
def Psychologist(request):
    return render(request ,"Psychologist.html")
def ophthalmology(request):
    return render(request ,"ophthalmology.html")
def nephrology(request):
    return render(request ,"nephrology.html")
def find_doctor(request):
    doctor = Doctor.objects.all()
    return render(request ,"find_doctor.html"  , {"doctor":doctor})

def profile(request , pk):
    doctor = Doctor.objects.get(pk=pk)
    return render(request ,"doctor_profile.html" , {"doctor":doctor})
def blood_bank(request):
    return render(request ,"blood_bank.html")
def ICU(request):
    return render(request ,"ICU.html")
def emergency_service(request):
    return render(request ,"emergency_service.html")
def dialysis_cantre(request):
    return render(request ,"dialysis_cantre.html")
def feedback(request):
    return render(request ,"feedback.html")
def equipment(request):
    return render(request ,"equipment.html")
def room(request):
    return render(request ,"room.html")
def about(request):
    return render(request ,"about.html")
def room(request):
    return render(request ,"room.html")
def contact(request):
    return render(request ,"contact.html")