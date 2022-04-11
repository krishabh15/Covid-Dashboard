from django.contrib import admin
from .models import DoctorVisit, FamilyVisit, MedicineList, Takeouts, Trips, PersonalData, TempData

admin.site.register(DoctorVisit)
admin.site.register(FamilyVisit)
admin.site.register(MedicineList)
admin.site.register(Trips)
admin.site.register(Takeouts)
admin.site.register(PersonalData)
admin.site.register(TempData)


# Register your models here.
