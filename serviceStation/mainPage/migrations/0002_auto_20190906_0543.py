# Generated by Django 2.2 on 2019-09-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(max_length=18, verbose_name='VIN'),
        ),
    ]