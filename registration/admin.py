from django.contrib import admin

# Register your models here.
from registration.models import StandUser, LicenceApplication, UserDocuments

admin.site.register(StandUser)
admin.site.register(LicenceApplication)
admin.site.register(UserDocuments)