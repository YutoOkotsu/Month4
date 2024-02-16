from . import views
from django.urls import path

urlpatterns = [
    path('shoe_list/', views.shoe_view, name='shoe_list'),
    path('shoe_detail/<int:id>/', views.shoe_shop_detail_view, name='shoe_detail'),
]
