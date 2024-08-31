from django.urls import path
from . import views

urlpatterns = [
    path('hello/' , views.say_hello),
    path('home/' , views.home),
    path('media/' , views.media),
    path('brain/' , views.brain),
    path('bone/' , views.bone),
    path('gastro/' , views.gastro),
    path('mother/' , views.mother),
    path('nephrologycenter/' , views.nephrologycenter),
    path('anesthesia/' , views.anesthesia),
    path('urology/' , views.urology),
    path('Psychologist/' , views.Psychologist),
    path('ophthalmology/' , views.ophthalmology),
    path('nephrology/' , views.nephrology),
    path('find_doctor/' , views.find_doctor),
    path('profile/' , views.profile),
    path('blood_bank/' , views.blood_bank),
    path('ICU/' , views.ICU),
    path('emergency_service/' , views.emergency_service),
    path('dialysis_cantre/' , views.dialysis_cantre),
    path('feedback/' , views.feedback),
    path('equipment/' , views.equipment),
    path('room/' , views.room),
    path('about/' , views.about),
    path('contact/' , views.contact),
]
