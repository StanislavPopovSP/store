from common.views import TitleMixin
from django.views.generic.edit import CreateView
from orders.forms import OrderForm

class OrderCreateView(TitleMixin, CreateView):
    """Оформление заказа"""
    template_name = 'orders/order-create.html'
    title = 'Store - Оформление заказа'
    form_class = OrderForm
