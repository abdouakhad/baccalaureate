from django.db import models
from liste.models import Liste
from jury.models import Jury
from django.contrib.auth.models import User
# Create your models here.


class Grade(models.Model):
    student = models.ForeignKey(Liste, on_delete=models.CASCADE)
    jury = models.ForeignKey(Jury, on_delete=models.CASCADE)
    grades = models.DecimalField(
        max_digits=6, decimal_places=3, blank=False, null=True)
    appreciations = models.CharField(max_length=100, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} {} {}'.format(self.student.student_number, self.student.first_name, self.student.last_name, self.grades)
