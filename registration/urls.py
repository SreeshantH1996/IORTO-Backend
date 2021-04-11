from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from registration import views

urlpatterns = [
    url(r'^login/$', views.UserLoginApiView.as_view(), name="login"),

    # USER REGISTRATION
    url(r'^user_registration/$', views.UserRegistrationApiView.as_view(), name="login"),
    # licence_apply
    url(r'^licence_apply/$', views.ApplicationForNewLicence.as_view(), name="apply_licence"),
    url(r'^get_user/$', views.GetUserDetails.as_view(), name="user_details  "),

]
