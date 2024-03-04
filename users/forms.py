from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, GENDER_TYPE, COLOR


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label='Укажите ваш номер')
    date_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), label='ДР')
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True, label='Гендер')
    favorite_color = forms.ChoiceField(choices=COLOR, label='Любимый цвет', )
    country = forms.CharField(required=False, label='Страна')
    city = forms.CharField(required=False, label='Город')
    address = forms.CharField(required=False, label='Адрес')
    position = forms.CharField(required=False, label='Должность')
    organization = forms.CharField(required=False, label='Организация')
    consent = forms.BooleanField(required=False, label='Согласие на обработку персональных данных')

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'date_birth',
            'gender', 'country', 'city', 'address', 'position', 'favorite_color'
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SMSCodeForm(forms.Form):
    code = forms.CharField(max_length=4)
