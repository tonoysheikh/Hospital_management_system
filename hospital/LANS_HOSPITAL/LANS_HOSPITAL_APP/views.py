from django.shortcuts import render
from django.http import HttpResponse

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
    doctors = {
        "doctor1" : {
            "name" : "Tanni",
            "speciality" : "Consultant, Dermatology",
            "degree" : "MBBS, DDV (SINGAPORE)"
        },
        "doctor2" : {
            "name" : "Dr. Rahul",
            "speciality" : "Medical Anthropology",
            "degree" : "MD (Doctor of Medicine), PhD (Doctor of Philosophy)"
        },
        "doctor3" : {
            "name" : "Dr. Nadiya",
            "speciality" : "Neurosurgery",
            "degree" : "MD (Doctor of Medicine), MPH (Master of Public Health)"
        },
       "doctor4" : {
            "name" : "Dr. Limon",
            "speciality" : "Virology",
            "degree" : "MD (Developer of the polio vaccine)"
        },
        "doctor5" : {
            "name" : "Dr. Halima",
            "speciality" : "Infectious Diseases",
            "degree" : "MD (Doctor of Medicine)"
        },
        "doctor6" : {
            "name" : "Dr. Krisna",
            "speciality" : "Pulmonology",
            "degree" : " MD (Inventor of the stethoscope)"
        },
        "doctor7" : {
            "name" :"Dr. Bidhan",
            "speciality" : "Pediatric Neurosurgery",
            "degree" : "MD (Doctor of Medicine)"
        },
        "doctor8" : {
            "name" :"Dr.Susmita",
            "speciality" : "Medical Anthropology",
            "degree" : "M.D., Ph.D."
        },
        "doctor9" : {
            "name" :"Dr. Kunal",
            "speciality" : "Ethology",
            "degree" : "Ph.D. (Although not a medical doctor, she is a doctor in her field)"
        },
        "doctor10" : {
            "name" :"Dr. Aniruddha",
            "speciality" : "Infectious Diseases",
            "degree" : "Doctor of Medicine (MD)"
        },
        "doctor11" : {
            "name" : "Dr. Rupali",
            "speciality" : "Cardiac Surgery",
            "degree" : "Doctor of Medicine (MD), PhD in Cardiothoracic Surgery"
        },
        "doctor12" : {
            "name" : "Dr. Kunal Sarkar",
            "speciality" : "Immunology",
            "degree" : "MD (Pioneer of the smallpox vaccine)"
        }

    }

    return render(request ,"find_doctor.html"  , doctors)

def profile(request):
    return render(request ,"doctor_profile.html")
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