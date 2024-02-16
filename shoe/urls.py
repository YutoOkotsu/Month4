from . import views
from django.urls import path

urlpatterns = [
    path('shoe_list/', views.shoe_view, name='shoe_list'),
]
