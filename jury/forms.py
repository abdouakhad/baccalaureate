from django.forms import ModelForm
from pages.models import Grade
# from jury.models import Jury
from liste.models import Liste
from django.forms import modelformset_factory
from django.contrib.auth.models import User


class GradeForm(ModelForm):

    class Meta:
        model = Grade
        fields = '__all__'
