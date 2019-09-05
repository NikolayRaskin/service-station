from django import forms
from mainPage.models import Customer

class CustomerForm(forms.ModelForm):
    birthDate = forms.DateField(
        label='Birth date',
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
        help_text = '(d/m/yyyy) format',
        )
    class Meta:
        model = Customer
        fields = ('firstName','lastName','birthDate','sex','address','phone','email','isReturn')