from django import forms
from . import models

class UpdateStudHealthForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = forms.ALL_FIELDS

    