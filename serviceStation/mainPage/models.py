from django.db import models
from django.shortcuts import redirect
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib import messages
import datetime
import re


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
    birthDate = models.DateField(_('Date of birth'))
    sex = models.CharField(_('Sex'), max_length=100, choices=SEX_CHOICES, default='M')
    address = models.CharField(_('Address'), max_length = 100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(_('Email:'),null=False, unique=True)
    isReturn = models.BooleanField(default=False)
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName

    def save(self, *args, **kwargs):
        today = datetime.date.today()
        if self.birthDate >= today:
            raise ValidationError('Birth Date isn\'t valid!')
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Car(models.Model):
    owner = models.ForeignKey(Customer, on_delete = models.CASCADE, null=True)
    make = models.CharField(_('Make '), max_length = 100)
    model = models.CharField(_('Model'), max_length = 100)
    yearOfСarManufacture = models.DateField(_('Year Of Сar Manufacture'), blank=True,null=False)
    vin = models.CharField(_('VIN'), max_length = 18, unique=True)
    
    def __str__(self):
        return self.owner.lastName + ': ' + self.model
    
    def save(self, *args, **kwargs):
        reg = '[-+!@#%^&,.:<>±§~]'
        if re.findall(reg, self.vin) != []:
            raise ValidationError('VIN isn\'t valid!')
        super().save(*args, **kwargs)

class Order(models.Model):
    orderCar = models.ForeignKey(Car, on_delete = models.PROTECT, null=True)
    orderOwner = models.ForeignKey(Customer, on_delete = models.PROTECT, null=True)
    orderDate = models.DateField(_('Date of order'),null=False)
    orderAmount = models.DecimalField(_('Order Amount'), max_digits = 10, decimal_places = 2)
    orderStatus = models.CharField(
        _('Order status'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='progress'
    )
    def __str__(self):
        return self.orderOwner.lastName + ' ' + self.orderCar.model + ': ' + self.orderStatus

    def save(self, *args, **kwargs):
        today = datetime.date.today()
        if self.orderDate < today:
            self.orderDate = today
        if self.orderAmount < 0.00:
            self.orderAmount = 0.00
        elif self.orderAmount > 10000.00:
            self.orderAmount = 10000.00
        super().save(*args, **kwargs)  # Call the "real" save() method.
