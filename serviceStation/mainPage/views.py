from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.db import models
from mainPage.models import Customer, Car, Order
from mainPage.addCustomerForm import CustomerForm
from customer_profile.addCarForm import CarForm
from customer_profile.addOrderForm import OrderForm
from django.core.exceptions import ValidationError

import datetime
import re

@login_required
def mainPage(request):
    try:
        customers = Customer.objects.all()
        cars = Car.objects.all()
        orders = Order.objects.all()
    except Customer.DoesNotExist:
        customers = 0
    except Car.DoesNotExist:
        customers = 0
    except Order.DoesNotExist:
        customers = 0
    context = {
        'customers':customers,
        'cars':cars,
        'orders':orders,
    }
    return render(request, 'mainPage/mainPage.html',context)

@login_required
def addCustomer(request):
    if request.method == 'POST':
        today = datetime.date.today()
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            birthDate = form.cleaned_data['birthDate']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            isReturn = form.cleaned_data['isReturn']
            if email_not_exists(email):
                newCustomer = Customer()
                newCustomer.firstName = firstName
                newCustomer.lastName = lastName
                newCustomer.birthDate = birthDate
                newCustomer.address = address
                newCustomer.phone = phone
                newCustomer.email = email
                newCustomer.isReturn = isReturn
                newCustomer.save(request)
            else:
                messages.info(request, 'Email already exists!')
            return redirect('/')
        else:
            messages.info(request, 'Form isn\'t valid!')
    else:
        form = CustomerForm()
    return render(request,'mainPage/addCustomerForm.html',{'form':form})

@login_required
def removeCustomer(request,id):
    customer = Customer.objects.get(pk=id)
    try:
        customer.delete()
    except models.ProtectedError:
        return render(request, 'customer_profile/afterProtectedError.html')
        # raise Http404('ProtectedError: You can\'t delete customer while it has car with active order.')
    return redirect('mainPage')

@login_required
def editCustomer(request,id):
    customer = Customer.objects.get(pk=id)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('mainPage')
    else:
        print('Form isn\'t valid!')
    context = {
        'form':form,
        'id':id,
    }
    return render(request,'mainPage/editCustomerForm.html',context)

@login_required
def addCar(request):
    if request.method == 'POST':
        form = CarForm(request.POST or None)
        if form.is_valid():
            owner = form.cleaned_data['owner']
            make = form.cleaned_data['make']
            model = form.cleaned_data['model']
            yearOfСarManufacture = form.cleaned_data['yearOfСarManufacture']
            vin = form.cleaned_data['vin']
            if vin_not_exists(vin):
                newCar = Car()
                newCar.owner = owner
                newCar.make = make
                newCar.model = model
                newCar.yearOfСarManufacture = yearOfСarManufacture
                newCar.vin = vin
                try:
                    newCar.save()
                except ValidationError:
                    messages.info(request, 'VIN isn\'t valid!')
            else:
                messages.info(request, 'VIN already exists!')
            return redirect('mainPage')
        else:
            messages.info(request, 'Form isn\'t valid!')
    else:
        form = CarForm()
    return render(request,'customer_profile/addCarForm.html',{'form':form})

@login_required
def addOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST or None)
        if form.is_valid():
            orderCar = form.cleaned_data['orderCar']
            orderDate = form.cleaned_data['orderDate']
            orderAmount = form.cleaned_data['orderAmount']
            orderStatus = form.cleaned_data['orderStatus']
            
            newOrder = Order()
            newOrder.orderCar = orderCar
            newOrder.orderOwner = orderCar.owner
            newOrder.orderDate = orderDate
            newOrder.orderAmount = orderAmount
            newOrder.orderStatus = orderStatus
            
            newOrder.save()
            return redirect('mainPage')
        else:
            messages.info(request, 'Form isn\'t valid!')
    else:
        form = OrderForm()
    return render(request,'customer_profile/addOrderForm.html',{'form':form})

def inputEmailError(request):
    return render(request,'mainPage/inputEmailError.html')
def inputVINError(request):
    return render(request,'mainPage/inputVINError.html')
def inputDateError(request):
    return render(request,'mainPage/inputDateError.html')

def email_not_exists(customer_email):
    if Customer.objects.filter(email=customer_email).exists():
        return False
    else:
        return True
def vin_not_exists(customer_vin):
    if Car.objects.filter(vin = customer_vin).exists():
        return False
    else:
        return True