from django.contrib import admin

# Register your models here.
from registration.models import Person, RtoOfficer

admin.site.register(Person)
admin.site.register(RtoOfficer)