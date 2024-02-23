from . import views
from django.urls import path

urlpatterns = [
    path('shoe_list/', views.shoe_view, name='shoe_list'),
    path('shoe_detail/<int:id>/', views.shoe_shop_detail_view, name='shoe_detail'),
    path('shoe_detail/<int:id>/delete/', views.delete_shoe_view, name='shoe_delete'),
    path('shoe_detail/<int:id>/update/', views.update_shoe_view, name='shoe_update'),
    path('creat_shoes/', views.creat_shoes_view, name='creat_shoes')
]
