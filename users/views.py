import random
import string
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms
from .forms import SMSCodeForm
from .models import SMSCode
from django.core.mail import send_mail


def generate_verification_code(length=4):
    return ''.join(random.choices(string.digits, k=length))


class RegistrationView(CreateView):
    form_class = forms.CustomRegisterForm
    success_url = '/confirm/'
    template_name = 'users/register.html'

    def form_valid(self, form):
        # Вызываем метод form_valid для обработки формы
        response = super().form_valid(form)

        # Достаем пользователя из формы
        user = form.save()

        # Генерируем и сохраняем код подтверждения
        verification_code = generate_verification_code()  # Предположим, что это ваша функция
        SMSCode.objects.create(user=user, code=verification_code)

        # Отправляем код подтверждения на почту
        send_mail(
            'Код подтверждения',
            f'Ваш код подтверждения: {verification_code}',
            'mc.oks1ne@gmail.com',
            [user.email],
            fail_silently=False,
        )

        return response


class ConfirmView(View):
    def get(self, request):
        form = SMSCodeForm()
        return render(request, 'users/confirm.html', {'form': form})

    def post(self, request):
        form = SMSCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            sms_code = SMSCode.objects.filter(code=code).first()

            if sms_code:
                sms_code.user.is_active = True
                sms_code.user.save()
                sms_code.delete()
                return redirect('shoe_list')
            else:
                form.add_error(None, 'Incorrect code')
        return render(request, 'users/confirm.html', {'form': form})


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return User.objects.all()


class LogOutView(LogoutView):
    next_page = reverse_lazy('users:home')