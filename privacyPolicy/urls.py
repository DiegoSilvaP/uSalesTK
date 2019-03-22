from django.urls import path
from .views import privacyDetailView

urlpatterns = [
    path('<int:pk>/<slug:slug>/', privacyDetailView.as_view(), name='privacy'),
]