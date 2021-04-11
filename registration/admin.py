from django.contrib import admin

# Register your models here.
from registration.models import StandUser, RtoOfficer

admin.site.register(StandUser)
admin.site.register(RtoOfficer)