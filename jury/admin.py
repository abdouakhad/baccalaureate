from django.contrib import admin

# Register your models here.
from .models import Jury


class JuryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'jury_number', 'phone_number')
    list_display_links = ('name', 'jury_number')
    list_filter = ('jury_number', 'name')
    liste_per_page = 25

    search_fields = ('jury_number', 'phone_number', 'jury_number')


admin.site.register(Jury, JuryAdmin)
