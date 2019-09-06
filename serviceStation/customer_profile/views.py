from django.shortcuts import render, redirect, HttpResponseRedirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.core.exceptions import ValidationError
from mainPage.models import Customer, Car, Order
from .addCarForm import CarForm
from .addOrderForm import OrderForm

@login_required
def customerProfile(request, id):
    numberOfCars = 0
    numberOfOrders = 0
    try:
        customer = Customer.objects.get(pk=id)
        car = Car.objects.filter(owner = customer)
        numberOfCars = car.count()
        order = Order.objects.filter(orderOwner = customer)
        numberOfOrders = order.count()
    except Car.DoesNotExist:
        car = 0
    except Order.DoesNotExist:
        order = 0
    context = {
        'customer':customer,
        'car':car,
        'order':order,
        'numberOfCars':numberOfCars,
        'numberOfOrders':numberOfOrders,
    }
    return render(request, 'customer_profile/profile.html', context)

@login_required
def removeCar(request,id):
    car = Car.objects.get(pk=id)
    car.delete()
    return redirect('mainPage')

@login_required
def editCar(request,id):
    car = Car.objects.get(pk=id)
    form = CarForm(request.POST or None, instance=car)
    if form.is_valid():
        try:
            form.save()
            return redirect('mainPage')
        except ValidationError:
            messages.info(request, 'VIN isn\'t valid!')

    context = {
        'form':form,
        'id':id,
    }
    return render(request,'customer_profile/editCarForm.html',context)

@login_required
def removeOrder(request,id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('mainPage')

@login_required
def editOrder(request,id):
    order = Order.objects.get(pk=id)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('mainPage')
    context = {
        'form':form,
        'id':id,
    }
    return render(request,'customer_profile/editOrderForm.html',context)
