from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    # Auth routes - login / register
    path("", include("apps.authentication.urls")),
    path("", include("apps.home.urls"))             # UI Kits Html files
    # path('', include('apps.home.urls')),
]
