from django.urls import path
from . import views

urlpatterns = [
    path('', views.parking_list, name="parking_list"),
    path("parking_reg/", views.parking_reg, name="parking_reg"),
    path('parking_list/edit/<int:pk>/', views.edit_parking_reg, name="edit_parking_reg"),
    path('parking_list/delete/<int:pk>/', views.delete_parking_reg, name="delete_parking_reg"),
]