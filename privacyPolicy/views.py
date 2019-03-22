from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Privacy

# Create your views here.
class privacyDetailView(DetailView):
    model = Privacy