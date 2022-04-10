from django.contrib import admin
from .models import DoctorVisit, FamilyVisit,MedicineList,Trips

admin.site.register(DoctorVisit)
admin.site.register(FamilyVisit)
admin.site.register(MedicineList)
admin.site.register(Trips)
# Register your models here.
