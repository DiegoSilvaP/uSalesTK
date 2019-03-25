from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import AboutUs, Privacy, FAQ

# Create your views here.
class AboutUsDetailView(DetailView):
    model = AboutUs

class PrivacyDetailView(DetailView):
    model = Privacy

class FAQListView(ListView):
    model = FAQ
