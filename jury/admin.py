from django.contrib import admin

# Register your models here.
from .models import Jury


class JuryAdmin(admin.ModelAdmin):
    # list_display = ('first_name', 'last_name', 'jury_number')
    # list_display_links = ('first_name', 'last_name', 'jury_number')
    list_filter = ('jury_number',)

    # search_fields = ('jury_number', 'first_name', 'last_name')


admin.site.register(Jury, JuryAdmin)
