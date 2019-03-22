from django.urls import path
from .views import informationDetailView

urlpatterns = [
    path('<int:pk>/<slug:slug>/', informationDetailView.as_view(), name='about_us'),
]