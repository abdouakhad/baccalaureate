from django.forms import ModelForm
from pages.models import Grade
# from jury.models import Jury
from liste.models import Liste
from django.forms import modelformset_factory
from django.contrib.auth.models import User


class GradeForm(ModelForm):
    # def __init__(self, jury=None, **kwargs):
    #     super(GradeForm, self).__init__(**kwargs)
    #     self.jury = jury
    #     self.fields['student'].queryset = Liste.objects.filter(
    #         jury_number=2)
    #     # self.fields['jury'].queryset = self.fields['jury'].queryset.exclude(
    #     #     jury_number=2)

    class Meta:
        model = Grade
        fields = '__all__'
