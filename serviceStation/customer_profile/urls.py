from django.urls import path,include
from . import views
from mainPage.models import Customer, Car, Order

urlpatterns = [
    path('<int:id>',views.customerProfile, name = 'customerProfile'),
    
    path('removeCar/<int:id>',views.removeCar, name = 'removeCar'),
    path('editCar/<int:id>',views.editCar, name = 'editCar'),

    path('removeOrder/<int:id>',views.removeOrder, name = 'removeOrder'),
    path('editOrder/<int:id>',views.editOrder, name = 'editOrder'),
]