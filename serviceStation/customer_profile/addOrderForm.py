from django import forms
from mainPage.models import Order

class OrderForm(forms.ModelForm):
    orderDate = forms.DateField(
        label='Date',
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y',),
        help_text = '(d/m/yyyy) format',
        )
    class Meta:
        model = Order
        fields = ('orderOwner','orderCar','orderDate','orderAmount','orderStatus')