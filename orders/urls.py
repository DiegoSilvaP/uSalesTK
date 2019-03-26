from django.urls import path
from .views import OrdersListView, OrderCreate

orders_patterns = ([
    path('',OrdersListView.as_view(), name='orders'),
    path('add/',OrderCreate.as_view(), name='addPurchase'),
    ],'orders')