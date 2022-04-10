from django.contrib import admin
from .models import DoctorVisit, FamilyVisit,MedicineList

admin.site.register(DoctorVisit)
admin.site.register(FamilyVisit)
admin.site.register(MedicineList)

# Register your models here.
