from django import forms
from mainPage.models import Order

class OrderForm(forms.ModelForm):
    orderDate = forms.DateField(
        label='Date',
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
        help_text = '(d/m/yyyy) format',
        )
    orderAmount = forms.DecimalField(label='Order amount',help_text = 'Between 0.00 and 10000.00')
    class Meta:
        model = Order
        fields = ('orderCar','orderDate','orderAmount','orderStatus')