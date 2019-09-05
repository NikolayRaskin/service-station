# Generated by Django 2.2 on 2019-09-05 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0005_customer_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', ' Female')], default='M', max_length=100, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderCar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainPage.Car'),
        ),
    ]