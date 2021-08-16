from django.db import models

# Create your models here.


class Liste (models.Model):
    SERIES = [
        ('L', 'L'),
        ('S', 'S'),
        ('T', 'T')
    ]

    student_number = models.IntegerField(null=False, blank=False)
    jury_number = models.PositiveIntegerField(null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(
        auto_now_add=False, null=False, blank=False)
    place_of_birth = models.CharField(max_length=100, null=False)
    school = models.CharField(max_length=100, null=True)
    serie = models.CharField(max_length=1, choices=SERIES, null=True)
    department = models.CharField(max_length=100, null=True, blank=False)
    ville = models.CharField(max_length=100, null=True, blank=False)
    region = models.CharField(max_length=100, null=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, (self.student_number))
