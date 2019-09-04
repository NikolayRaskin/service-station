from django import forms
from mainPage.models import Car

class CarForm(forms.ModelForm):
    yearOfСarManufacture = forms.DateField(
        label='Date',
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
        help_text = '(d/m/yyyy) format',
        )
    class Meta:
        model = Car
        fields = ('owner','make','model','yearOfСarManufacture','vin')