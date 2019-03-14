from django.urls import path
from .views import Shopping_basketListView, Shopping_basketItemAdd, Shopping_basketItemDelete, Shopping_basketItemUpdate


shopping_basket_patterns = ([
    path('', Shopping_basketListView.as_view(), name="shopping_basket_list"),
    path('add/', Shopping_basketItemAdd.as_view(), name="addBasket_listItem"),
    path('update/', Shopping_basketItemUpdate.as_view(), name="updateBasket_listItem"),
    path('delete/', Shopping_basketItemDelete.as_view(), name="deleteBasket_listItem"),
    
], 'shopping_basket')