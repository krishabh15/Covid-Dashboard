from pyexpat import model
from django.db import models

# Create your models here.

class DoctorVisit(models.Model):
    doctor = models.CharField('Doctor Name', max_length=120)
    visit_date = models.DateField('Visit Date', blank=True, null=True)
    reason = models.CharField(
        'Reason of Visit', max_length=500, blank=True, null=True)
    notes = models.CharField('Notes', max_length=500, blank=True, null=True)
    user = models.IntegerField('id', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.doctor


class FamilyVisit(models.Model):
    location = models.CharField('location', max_length=120)
    noofpeople = models.CharField(
        'No of people', max_length=500, blank=True, null=True)
    date = models.DateField('date', blank=True, null=True)
    time = models.CharField('time', max_length=500, blank=True, null=True)
    reason = models.CharField('reason', max_length=500, blank=True, null=True)
    user = models.IntegerField('id', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.location


class MedicineList(models.Model):
    medicine = models.CharField('Medicine', max_length=120)
    Nooftimesaday = models.CharField(
        'No of times a day', max_length=500, blank=True, null=True)
    fromdate = models.DateField('from', blank=True, null=True)
    to = models.DateField('to', blank=True, null=True)
    reason = models.CharField('reason', max_length=500, blank=True, null=True)
    user = models.IntegerField('id', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.medicine


class Trips(models.Model):
    destination = models.CharField('Destination', max_length=120)
    duration = models.IntegerField(
        'Duration', max_length=500, blank=True, null=True)
    fromdes = models.DateField('From', blank=True, null=True)
    to = models.DateField('To', blank=True, null=True)
    user = models.IntegerField('id', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.destination


class Takeouts(models.Model):
    restaurant = models.CharField('Restaurant / Cafe', max_length=120)
    type = models.CharField('Type', max_length=500, blank=True, null=True)
    date = models.DateField('Date', blank=True, null=True)
    time = models.TimeField('Time', blank=True, null=True)
    user = models.IntegerField('id', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.restaurant


class PersonalData(models.Model):
    vaccine = models.CharField('Vaccine', max_length=120)
    dose1 = models.DateField('Dose 1', blank=True, null=True)
    dose2 = models.DateField('Dose 2', blank=True, null=True)
    booster = models.DateField('Booster', blank=True, null=True)
    notes = models.CharField('Notes', max_length=500, blank=True, null=True)
    user = models.IntegerField('id', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.vaccine


class TempData(models.Model):
    temp = models.CharField('Temperature', max_length=120)
    date = models.DateField('Date', blank=True, null=True)
    time = models.TimeField('Time', blank=True, null=True)
    notes = models.CharField('Notes', max_length=500, blank=True, null=True)
    user = models.IntegerField('id', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.temp
