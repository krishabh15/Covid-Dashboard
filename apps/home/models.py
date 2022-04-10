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


class DoctorVisit(models.Model):
    doctor = models.CharField('Doctor Name', max_length=120)
    visit_date = models.DateField('Visit Date', blank=True, null=True)
    reason = models.CharField('Reason of Visit', max_length=500, blank=True, null=True)
    notes = models.CharField('Notes', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.doctor
