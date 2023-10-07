from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('task/', views.home, name='home'),
    path('addTask/', views.add_task, name='addTask'),
    path('deleteTask/<int:pk>/', views.delete_task, name='deleteTask'),
]
