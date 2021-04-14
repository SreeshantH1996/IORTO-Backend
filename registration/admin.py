from django.contrib import admin

# Register your models here.
from registration.models import *

admin.site.register(StandUser)
admin.site.register(LicenceApplication)
admin.site.register(UserDocuments)
admin.site.register(OtherDocuments)
admin.site.register(LicenceRenewalApplication)
admin.site.register(RtoOfficer)
