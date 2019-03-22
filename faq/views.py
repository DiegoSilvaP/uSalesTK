from django.shortcuts import render
from .models import FAQ
from django.views.generic.list import ListView

# Create your views here.
class FAQListView(ListView):
    model = FAQ
