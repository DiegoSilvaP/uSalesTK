from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import AboutUs

# Create your views here.
class informationDetailView(DetailView):
    model = AboutUs