from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('task', views.home, name='home'),
]
