from django.urls import path
from .views import OrdersListView, OrderCreate, OrderUpdate

orders_patterns = ([
    path('',OrdersListView.as_view(), name='orders'),
    path('add/',OrderCreate.as_view(), name='addPurchase'),
    path('fisnish-order/<int:pk>/',OrderUpdate.as_view(), name='updatePurchase'),
    ],'orders')