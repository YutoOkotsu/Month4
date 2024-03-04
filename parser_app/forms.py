from django import forms
from .models import ParserModel
from . import parser_1

class ParserForm(forms.Form):
    MEDIA_CHOICES = [
        ("manas.kg", "manas.kg"),
    ]
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ("media_type",)

    def parser_data(self):
        if self.data["media_type"] == "manas.kg":
            film_parser = parser_1.parser()
            for i in film_parser:
                ParserModel.objects.create(**i)