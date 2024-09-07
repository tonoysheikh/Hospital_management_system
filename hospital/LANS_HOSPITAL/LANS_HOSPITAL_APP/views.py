from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor
from .models import Room
from .models import Feedback
from .models import Contact
from .models import Information

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
    search_term = request.GET.get("search", "").strip()
    
    if search_term:
        search_todo = Doctor.objects.filter(name__icontains=search_term)
    else:
        search_todo = Doctor.objects.all()
    
    context = {
        "search_todo": search_todo,
    }
    
    return render(request, "find_doctor.html", context)

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
    information = Information.objects.all().first()  
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        feedback = Feedback(name=name, email=email, subject=subject, feedback=message)
        feedback.save()

    context = {
        "information": information,
        "Email": information.Email if information else "",  
        "Help_center": information.Help_center if information else "",  
        "Touch": information.touch if information else "", 
        "Address": information.Address if information else "",
        "care_line" : information.Care_Line if information else "",
    }
    
    return render(request, "feedback.html", context)

def lay(request):
    information = Information.objects.all().first()  
    
    context = {
        "information": information,
        "Email": information.Email if information else "",  
        "Address": information.address if information else "", 
        "care_line" : information.care_line if information else "",  
    }
    return render(request, "lay.html", context)



def equipment(request):
    return render(request ,"equipment.html")
def about(request):
    return render(request ,"about.html")
def room(request):
    rooms = Room.objects.all()
    return render(request ,"room.html" , {"rooms": rooms})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create a new patient entry in the database using the Patient model
        contact = Contact(name=name, email=email, subject = subject, message = message)
        contact.save()
        
    return render(request ,"contact.html")