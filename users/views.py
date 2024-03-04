from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from . import forms


class HomepageView(TemplateView):
    template_name = 'users/homepage.html'


class RegistrationView(CreateView):
    form_class = forms.CustomRegisterForm
    # form_class = UserCreationForm
    success_url = '/homepage/'
    template_name = 'users/register.html'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:post')


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'users/user_list.html'

    def get_queryset(self):
        return User.objects.all()


class LogOutView(LogoutView):
    next_page = reverse_lazy('users:home')


