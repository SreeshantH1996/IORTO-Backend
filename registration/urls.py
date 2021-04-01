from django.contrib import admin
from django.urls import path, include

from registration import views

urlpatterns = [
    path('user_registration/', views.user_registration, name='user_registration'),
    path('user_login/', views.user_login, name='user_login'),
]