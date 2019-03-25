from django.urls import path
from .views import AboutUsDetailView, PrivacyDetailView, FAQListView

information_patterns = ([
    path('about-us/<int:pk>/<slug:slug>/', AboutUsDetailView.as_view(), name='about_us'),
    path('privacy-policies/<int:pk>/<slug:slug>/', PrivacyDetailView.as_view(), name='privacy'),
    path('faq/', FAQListView.as_view(), name='FAQ'),
], 'information')