from django.urls import path
from .views import Wish_listListView, Wish_listAdd, Wish_listDelete
from . import views


wish_list_patterns = ([
    path('', Wish_listListView.as_view(), name="wish_lists"),
    path('add/', Wish_listAdd.as_view(), name="addWish_listItem"),
    path('delete/', Wish_listDelete.as_view(), name="deleteWish_listItem"),
], 'wish_lists')