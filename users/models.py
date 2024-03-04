from django.db import models
from django.contrib.auth.models import User

GENDER_TYPE = (
    ('Мужчина', 'Мужчина'),
    ('Женщина', 'Женщина')
)

COLOR = (
    ('красный', 'Красный'),
    ('зеленый', 'Зеленый'),
    ('синий', 'Синий'),
    ('желтый', 'Желтый'),
    ('черный', 'Черный'),
    ('белый', 'Белый'),
)


class CustomUser(User):
    phone_number = models.CharField(max_length=13,
                                    default='+996', verbose_name='Введите номер телефона')
    date_birth = models.DateField(verbose_name='Ваша дата рождения')
    gender = models.CharField(choices=GENDER_TYPE, max_length=20, verbose_name='Укажите пол')
    favorite_color = models.CharField(choices=COLOR, max_length=255, verbose_name='Любимый цвет', )
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    position = models.CharField(max_length=255, verbose_name='Должность')
    organization = models.CharField(max_length=255, verbose_name='Организация')
    consent = models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных')


class SMSCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sms_codes')
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.code}'