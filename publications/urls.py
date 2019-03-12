from django.urls import path
from .views import PublicationListView, PublicationDetailView, PublicationCreate, PublicationUpdate

publications_patterns = ([
    path('', PublicationListView.as_view(), name='publications'),
    # path('multiple/', MultipleModelView.as_view(), name='multiple'),
    path('publication/<int:pk>/<slug:slug>/', PublicationDetailView.as_view(), name='publication'),
    path('create/', PublicationCreate.as_view(), name='create'),
    path('update/<int:pk>/', PublicationUpdate.as_view(), name='update'),
    ], 'publications')