from django.contrib import admin

# Register your models here.
from .models import Information
from .models import Doctor
from .models import Room
from .models import Feedback
from .models import Contact
from .models import Appointment

admin.site.register(Information)
admin.site.register(Doctor)
admin.site.register(Room)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(Appointment)