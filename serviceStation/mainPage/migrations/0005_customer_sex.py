# Generated by Django 2.2 on 2019-09-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0004_auto_20190905_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('W', ' Women')], default='M', max_length=100, verbose_name='Sex'),
        ),
    ]
