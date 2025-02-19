from django.contrib import admin

# Register your models here.
from .models import Note, SharedNote



admin.site.register(Note)
admin.site.register(SharedNote) 
