from django.db import models
from liste.models import Liste
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.


class Jury(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    # liste = models.ForeignKey(Liste, on_delete=models.DO_NOTHING)
    jury_number = models.PositiveIntegerField(null=False, blank=False)
    date_of_birth = models.DateField(
        auto_now_add=False, null=False, blank=False, default=0)
    place_of_birth = models.CharField(max_length=100, null=False)
    school_affected = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=30, default=0)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):

        # Do something()
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{} {} {}'.format(self.user.first_name, self.user.last_name, -self.jury_number)
