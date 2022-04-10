from django.contrib import admin
from .models import DoctorVisit, FamilyVisit,MedicineList, Takeouts,Trips

admin.site.register(DoctorVisit)
admin.site.register(FamilyVisit)
admin.site.register(MedicineList)
admin.site.register(Trips)
admin.site.register(Takeouts)
# Register your models here.
