from django.contrib import admin

# Register your models here.

from .models import Liste
from django.forms import ModelForm

class ListeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_number', 'jury_number')
    list_display_links = ('first_name', 'last_name', 'student_number', 'jury_number')
    list_filter = ('student_number','jury_number')
    search_fields = ('student_number', 'jury_number','first_name', 'last_name')

admin.site.register(Liste, ListeAdmin) 
