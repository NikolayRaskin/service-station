from django import forms
from mainPage.models import Car

class CarForm(forms.ModelForm):
    yearOfСarManufacture = forms.DateField(
        label='Date',
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
        help_text = '(d/m/yyyy) format'
        )
    vin = forms.CharField(max_length=17, min_length=17,help_text = '17 symbols',)
    class Meta:
        model = Car
        fields = ('owner','make','model','yearOfСarManufacture','vin')