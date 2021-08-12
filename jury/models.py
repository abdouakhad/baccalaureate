from django.db import models
from liste.models import Liste
from django.forms import ModelForm
# Create your models here.

class Jury(models.Model):
    liste = models.ForeignKey(Liste, on_delete=models.DO_NOTHING) 
    jury_number = models.PositiveIntegerField( null = False, blank = False)
    first_name = models.CharField(max_length=100, null = False, blank = False)
    last_name = models.CharField(max_length=100, null = False, blank = False)
    # date_of_birth = models.DateField(auto_now_add=False, null = False, blank = False, input_formats = ["%d-%m-%Y",])
    place_of_birth = models.CharField(max_length=100, null = False)
    school_affected = models.CharField(max_length=100, null = False)
    phone_number = models.CharField(max_length=30)
    grades = models.DecimalField(max_digits = 6, decimal_places = 3)
    appreciations = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        # Do something()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.jury_number)