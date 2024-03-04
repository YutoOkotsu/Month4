from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='post'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm'),
]