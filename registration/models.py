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


class Person(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False, default="test")
    age = models.IntegerField(null=False, blank=False, default="1")
    district = models.CharField(choices=district_choices, verbose_name='Order Status', max_length=50)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)


class RtoOfficer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phnumber = models.IntegerField(null=True, blank=True)
    officerid = models.CharField(max_length=30, null=False, blank=False)
    district = models.CharField(choices=district_choices, verbose_name='Order Status', max_length=50)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
