from django.contrib import admin
from django.urls import path, include

from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('registration.urls', 'registration'), namespace='registration')),
    path('api-auth/', include('rest_framework.urls')),

]
