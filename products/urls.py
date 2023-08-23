from django.urls import path
from products.views import products, basket_add, basket_remove


app_name = 'products'
urlpatterns = [
     path('', products, name='products'),
     path('category/<int:category_id>/', products, name='category'),
     path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),  # ..products/baskets/add/<products_id>/
     path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove')
]
