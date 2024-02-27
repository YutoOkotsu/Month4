from . import views
from django.urls import path

urlpatterns = [
    path('shoe_list/', views.ShoeView.as_view(), name='shoe_list'),
    path('shoe_detail/<int:id>/', views.ShoeDetailView.as_view(), name='shoe_detail'),
    path('shoe_detail/<int:id>/delete/', views.DeleteShoeView.as_view(), name='shoe_delete'),
    path('shoe_detail/<int:id>/update/', views.UpdateShoeView.as_view(), name='shoe_update'),
    path('creat_shoes/', views.CreateShoeView.as_view(), name='creat_shoes')
]
