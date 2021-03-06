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

user_status = [
    ("Application Filled", "Application Filled"),
    ("Documents Uploaded", "Documents Uploaded"),
    ("Payment Completed, Waiting for approval", "Payment Completed, Waiting for approval"),
    ("Approved", "Approved"),
    ("Not yet Applied", "Not yet Applied"),
]


class StandUser(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False, default="test")
    age = models.CharField(max_length=50,null=False, blank=False, default="1")
    phnumber = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(choices=district_choices, verbose_name='Order Status', max_length=50)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    user_status = models.CharField(choices=user_status, verbose_name='User Status', default="Not yet Applied",
                                   max_length=500)
    renewal_status = models.CharField(max_length=50, null=True, blank=True)


class RtoOfficer(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phnumber = models.CharField(max_length=10, null=True, blank=True)
    officerid = models.CharField(max_length=30, null=False, blank=False)
    district = models.CharField(choices=district_choices, verbose_name='Order Status', max_length=50)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)


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
    reasonforrejecting = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(max_length=50, null=True, blank=True)



class UserDocuments(models.Model):
    user = models.ForeignKey(StandUser, null=False, on_delete=models.CASCADE)

    identitycertificate = models.FileField(blank=True, null=True, upload_to='static/Files/%Y/%m/%d/',
                                           verbose_name='identification certificate')
    identitytype = models.CharField(max_length=50, null=True, blank=True)
    eyecertificate = models.FileField(blank=True, null=True, upload_to='static/Files/%Y/%m/%d/',
                                      verbose_name='eye certificate')
    medicalcertificate = models.FileField(blank=True, null=True, upload_to='static/Files/%Y/%m/%d/',
                                          verbose_name='medical certificate')
    selfcertificate = models.FileField(blank=True, null=True, upload_to='static/Files/%Y/%m/%d/',
                                       verbose_name='self certificate')
    photo = models.ImageField(blank=True, null=True, upload_to='static/Images/Photo/',
                              verbose_name='photo')
    signature = models.FileField(blank=True, null=True, upload_to='static/Images/Signature/',
                                 verbose_name='signature ')


class OtherDocuments(models.Model):
    user = models.ForeignKey(StandUser, null=False, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100, null=True, blank=True)
    document = models.FileField(blank=True, null=True, upload_to='static/Files/Other_Documents',
                                verbose_name='other document')


class LicenceRenewalApplication(models.Model):
    user = models.ForeignKey(StandUser, null=False, on_delete=models.CASCADE)
    district = models.CharField(choices=district_choices, verbose_name='Order Status', max_length=50)
    phnumber = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    dob = models.DateTimeField(null=False, blank=False)
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
    licencenumber = models.CharField(max_length=100, null=False, blank=False)
    licencefrom = models.DateTimeField(null=False, blank=False)
    licenceto = models.DateTimeField(null=False, blank=False)
    reasonforrejecting = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.CharField(max_length=50, null=True, blank=True)
