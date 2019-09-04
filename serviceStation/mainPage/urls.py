from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static

from django.urls import path,include
from . import views
from mainPage.models import Customer, Car, Order

urlpatterns = [
    path('',views.mainPage, name = 'mainPage'),
    path('addCustomer/',views.addCustomer, name = 'addCustomer'),
    path('removeCustomer/<int:id>',views.removeCustomer, name = 'removeCustomer'),
    path('editCustomer/<int:id>',views.editCustomer, name = 'editCustomer'),

    path('addOrder/',views.addOrder, name = 'addOrder'),
    path('addCar/',views.addCar, name = 'addCar'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)