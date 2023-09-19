from django import forms

from orders.models import Order

# Создадим форму, которая будет работать с классом Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')
