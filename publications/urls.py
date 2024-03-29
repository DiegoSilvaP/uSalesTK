from django.urls import path
from .views import PublicationListView, PublicationDetailView, PublicationCreate, PublicationUpdate, PublicationListSearchView, PublicationDelete, getSubCategory

publications_patterns = ([
    path('', PublicationListView.as_view(), name='publications'),
    path('get_sub_category/', getSubCategory.as_view(), name='getSubCategory'),
    path('search/', PublicationListSearchView.as_view(), name='search'),
    path('publication/<int:pk>/<slug:slug>/', PublicationDetailView.as_view(), name='publication'),
    path('create/', PublicationCreate.as_view(), name='create'),
    path('update/<int:pk>/', PublicationUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PublicationDelete.as_view(), name='delete'),
    ], 'publications')