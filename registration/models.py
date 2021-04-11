from django.db import models

# Create your models here.
district_choices = [
    ('Alappuzha', 'Alappuzha'),
    ('Ernakulam', 'Ernakulam'),
    ('Idukki', 'Idukki'),
    ('Kannur', 'Kannur'),
    ('Kasaragod', 'Kasaragod'),
    ('Kollam', 'Kollam'),
    ('Kottayam', 'Kottayam'),
    ('Kozhikode', 'Kozhikode'),
    ('Malappuram', 'Malappuram'),
    ('Palakkad', 'Palakkad'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Thrissur', 'Thrissur'),
    ('Wayanad', 'Wayanad')
]


class StandUser(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False, default="test")
    age = models.IntegerField(null=False, blank=False, default="1")
    district = models.CharField(choices=district_choices, verbose_name='Order Status', max_length=50)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)


class RtoOfficer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phnumber = models.CharField(max_length=10, null=True, blank=True)
    officerid = models.CharField(max_length=30, null=False, blank=False)
    district = models.CharField(choices=district_choices, verbose_name='Order Status', max_length=50)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)


class LicenceApplication(models.Model):
    user = models.ForeignKey(StandUser, null=False, on_delete=models.CASCADE)
    district = models.CharField(choices=district_choices, verbose_name='Order Status', max_length=50)
    phnumber = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    relation_with = models.CharField(max_length=50, null=False, blank=False)
    relation_name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=50, null=False, blank=False)
    qualification = models.CharField(max_length=100, null=False, blank=False)
    emphnumber = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateTimeField(null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    blood = models.CharField(max_length=50, null=False, blank=False)
    identificationmark1 = models.CharField(max_length=500, null=False, blank=False)
    identificationmark2 = models.CharField(max_length=500, null=False, blank=False)
    prhousename = models.CharField(max_length=100, null=False, blank=False)
    prstreet = models.CharField(max_length=100, null=False, blank=False)
    prlocation = models.CharField(max_length=100, null=False, blank=False)
    prpincode = models.CharField(max_length=100, null=False, blank=False)
    prvillage = models.CharField(max_length=100, null=False, blank=False)
    prtaluk = models.CharField(max_length=100, null=False, blank=False)
    trhousename = models.CharField(max_length=100, null=False, blank=False)
    tstreet = models.CharField(max_length=100, null=False, blank=False)
    trlocation = models.CharField(max_length=100, null=False, blank=False)
    trpincode = models.CharField(max_length=100, null=False, blank=False)
    trvillage = models.CharField(max_length=100, null=False, blank=False)
    trtaluk = models.CharField(max_length=100, null=False, blank=False)
    classofvehicle = models.CharField(max_length=100, null=False, blank=False)
