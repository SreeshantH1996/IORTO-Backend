from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from registration import views

urlpatterns = [
    url(r'^login/$', views.UserLoginApiView.as_view(), name="login"),


    # USER REGISTRATION
    url(r'^user_registration/$', views.UserRegistrationApiView.as_view(), name="login"),
]
