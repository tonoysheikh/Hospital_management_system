from django.contrib import admin

# Register your models here.

from .models import Doctor
from .models import Room

admin.site.register(Doctor)
admin.site.register(Room)