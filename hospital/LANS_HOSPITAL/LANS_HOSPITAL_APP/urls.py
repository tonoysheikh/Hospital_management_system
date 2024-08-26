from django.urls import path
from . import views

urlpatterns = [
    path('hello/' , views.say_hello),
    path('home/' , views.home),
    path('media/' , views.media),
    path('brain/' , views.brain),
    path('brain/' , views.bone),
    path('brain/' , views.gastro),
    path('brain/' , views.mother),
    path('brain/' , views.nephrologycenter),
    path('brain/' , views.anesthesia),
    path('brain/' , views.urology),
    path('brain/' , views.Psychologist),
    path('brain/' , views.ophthalmology),
    path('brain/' , views.nephrology),
    path('brain/' , views.find_doctor),
    path('brain/' , views.blood_bank),
    path('brain/' , views.ICU),
    path('brain/' , views.emergency_service),
    path('brain/' , views.dialysis_cantre),
    path('brain/' , views.feedback),
    path('brain/' , views.equipment),
    path('brain/' , views.room),
    path('brain/' , views.about),
    path('brain/' , views.contact),
]
