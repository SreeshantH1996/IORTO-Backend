from django.contrib import admin

# Register your models here.
from registration.models import StandUser,  LicenceApplication

admin.site.register(StandUser)
admin.site.register(LicenceApplication)