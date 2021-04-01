from django.contrib import admin
from django.urls import path, include

from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include(('registration.urls', 'registration'), namespace='registration'))
]
