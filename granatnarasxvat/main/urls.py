from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delivery', views.delivery, name='delivery'),
    path('bouquets', views.bouquets, name='bouquets'),
    path('order', views.order, name='order'),
    path('order-success', views.orderSuccess, name='order-success')
]