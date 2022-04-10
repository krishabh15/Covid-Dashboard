from urllib import request
from django.db import models

# Create your models here.

# class User_Detail(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=254)
#     phone = models.CharField(max_length=20)
#     message = models.TextField(max_length=500)
#     contacted = models.BooleanField(default=False)

#     def __str__(self):
#         return '{}'.format(self.name)

# curr_user = request.user

class DoctorVisit(models.Model):
    doctor = models.CharField('Doctor Name', max_length=120)
    visit_date = models.DateField('Visit Date', blank=True, null=True)
    reason = models.CharField('Reason of Visit', max_length=500, blank=True, null=True)
    notes = models.CharField('Notes', max_length=500, blank=True, null=True)
    user = models.IntegerField('id', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.doctor

class FamilyVisit(models.Model):
    location = models.CharField('location', max_length=120)
    noofpeople = models.CharField('No of people', max_length=500, blank=True, null=True)
    date = models.DateField('date', blank=True, null=True)
    time = models.CharField('time', max_length=500, blank=True, null=True)
    reason = models.CharField('reason', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.location

class MedicineList(models.Model):
    medicine = models.CharField('Medicine', max_length=120)
    Nooftimesaday = models.CharField('No of times a day', max_length=500, blank=True, null=True)
    fromdate = models.DateField('from', blank=True, null=True)
    to = models.DateField('to', blank=True, null=True)
    reason = models.CharField('reason', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.medicine
