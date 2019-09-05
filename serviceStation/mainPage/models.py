from django.db import models
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from phone_field import PhoneField

STATUS_CHOICES = (
    ('cancelled', 'Cancelled'),
    ('progress', ' In Progress'),
    ('completed', 'Completed')
)

SEX_CHOICES = (
    ('M', 'Male'),
    ('F', ' Female')
)

class Customer(models.Model):
    firstName = models.CharField(_('First name'), max_length = 100)
    lastName = models.CharField(_('Last name'), max_length = 100)
    birthDate = models.DateTimeField(_('Date of birth'))
    sex = models.CharField(_('Sex'), max_length=100, choices=SEX_CHOICES, default='M')
    address = models.CharField(_('Address'), max_length = 100)
    phone = models.CharField(_('Phone'), max_length = 20)
    email = models.EmailField(_('Email:'),null=False)
    # avatar = models.ImageField(upload_to='avatars/', blank=True)
    isReturn = models.BooleanField(default=False)
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Car(models.Model):
    owner = models.ForeignKey(Customer, on_delete = models.CASCADE, null=True)
    make = models.CharField(_('Make '), max_length = 100)
    model = models.CharField(_('Model'), max_length = 100)
    yearOfСarManufacture = models.DateTimeField(_('Year Of Сar Manufacture'), blank=True,null=False)
    vin = models.IntegerField(_('VIN'))
    def __str__(self):
        return self.owner.lastName + ': ' + self.model

class Order(models.Model):
    orderCar = models.ForeignKey(Car, on_delete = models.PROTECT, null=True)
    orderOwner = models.ForeignKey(Customer, on_delete = models.PROTECT, null=True)
    orderDate = models.DateField(_('Date of order'),null=False)
    orderAmount = models.DecimalField(_('Order Amount'), max_digits = 10, decimal_places = 2)
    orderStatus = models.CharField(
        _('Order status'),
        max_length=100,
        choices=STATUS_CHOICES,
        default='progress'
    )
    def __str__(self):
        return self.orderOwner.lastName + ' ' + self.orderCar.model + ': ' + self.orderStatus