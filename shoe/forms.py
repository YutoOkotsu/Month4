from django import forms
from . import models


class ShoesForm(forms.ModelForm):
    class Meta:
        model = models.Shoe
        fields = '__all__'


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = models.CommentShoe
        fields = ('text', 'shoe_comment')
