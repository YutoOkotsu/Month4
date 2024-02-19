from django import forms
from . import models


class ShoesForm(forms.ModelForm):
    class Meta:
        model = models.Shoe
        fields = '__all__'
