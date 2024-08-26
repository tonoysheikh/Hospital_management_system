from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello, world')

def home(request):
    return render(request, "index.html")

def media(request):
    return render(request ,"media.html")

def test(request):
    return render(request ,"brain.html")
def test(request):
    return render(request ,"bone.html")
def test(request):
    return render(request ,"gastro.html")
def test(request):
    return render(request ,"mother.html")
def test(request):
    return render(request ,"nephrologycenter.html")
def test(request):
    return render(request ,"anesthesia.html")
def test(request):
    return render(request ,"urology.html")
def test(request):
    return render(request ,"Psychologist.html")
def test(request):
    return render(request ,"ophthalmology.html")
def test(request):
    return render(request ,"nephrology.html")
def test(request):
    return render(request ,"find_doctor.html")
def test(request):
    return render(request ,"blood_bank.html")
def test(request):
    return render(request ,"ICU.html")
def test(request):
    return render(request ,"emergency_service.html")
def test(request):
    return render(request ,"dialysis_cantre.html")
def test(request):
    return render(request ,"feedback.html")
def test(request):
    return render(request ,"equipment.html")
def test(request):
    return render(request ,"room.html")
def test(request):
    return render(request ,"about.html")
def test(request):
    return render(request ,"room.html")
def test(request):
    return render(request ,"contact.html")