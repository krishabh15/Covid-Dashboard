from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # # Matches any html file

    path('doctors', views.doctor_visits, name='doctors'),
    path('family', views.family_visits, name='family'),
    path('medicines', views.medicine, name='medicines'),
    path('trips', views.trips, name='trips'),
    path('takeouts', views.takeouts, name='takeouts'),

    # path('personal-data', views.personal_data, name='personal-data'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]
