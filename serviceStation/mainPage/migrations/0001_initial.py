# Generated by Django 2.2 on 2019-09-21 13:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100, verbose_name='Make ')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('yearOfСarManufacture', models.DateField(blank=True, verbose_name='Year Of Сar Manufacture')),
                ('vin', models.CharField(max_length=18, verbose_name='VIN')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100, verbose_name='First name')),
                ('lastName', models.CharField(max_length=100, verbose_name='Last name')),
                ('birthDate', models.DateField(verbose_name='Date of birth')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', ' Female')], default='M', max_length=100, verbose_name='Sex')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, verbose_name='Email:')),
                ('isReturn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField(verbose_name='Date of order')),
                ('orderAmount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Order Amount')),
                ('orderStatus', models.CharField(choices=[('cancelled', 'Cancelled'), ('progress', ' In Progress'), ('completed', 'Completed')], default='progress', max_length=20, verbose_name='Order status')),
                ('orderCar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainPage.Car')),
                ('orderOwner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainPage.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainPage.Customer'),
        ),
    ]
