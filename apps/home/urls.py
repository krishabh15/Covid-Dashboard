from django.urls import path, re_path
from apps.home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    #
    # # Matches any html file
    #
    # # path('doctors', views.doctors, name="doctors"),
    # path('medicines/', views.medicines, name="medicines"),

    path('doctors', views.doctor_visits, name='doctors'),
    path('family', views.family_visits, name='family'),
    path('medicines', views.medicine, name='medicines'),
    re_path(r'^.*\.*', views.pages, name='pages'),

]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about', views.about, name="about"),
#     path('products', views.product, name="products"),
#     path('training', views.training, name="training"),
#     path('contact', views.contact, name="contact"),
#     path('search', views.search, name="search"),
#     path("products/<slug>", views.product_view, name="product_view"),
#     path("products/sterilization/<ster_slug>",
#          views.ster_product_view, name="ster_product_view"),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = urlpatterns + \
#     static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
