from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Wish_listItem
from publications.models import Publication
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic import View

from django.contrib.auth.models import User
from django.core import serializers


from django.http import JsonResponse



# Create your views here.
class Wish_listListView(ListView):
    model = Wish_listItem
    def get_context_data(self, **kwargs):
        context = super(Wish_listListView, self).get_context_data(**kwargs)
        context['wish_list'] = Wish_listItem.objects.filter(customer=self.request.user).values_list("publication").values()
        if self.request.user.is_anonymous !=True:
            context['publications'] = Publication.objects.all().values_list("product").values()
        return context


class Wish_listAdd(View):
    def get(self, request, *args, **kwargs):
        publication = request.GET['publication']
        # customer = request.GET['customer']
        _publication = Publication.objects.get(id=publication)
        _customer = self.request.user
        Wish_listItem(customer = _customer,publication=_publication).save()
        data = {
            'result': 1
        }
        return JsonResponse(data)

class Wish_listDelete(View):
    def get(self, request, *args, **kwargs):
        publication = request.GET['publication']
        # customer = request.GET['customer']
        _publication = Publication.objects.get(id=publication)
        _customer = self.request.user
        Wish_listItem.objects.get(customer = _customer,publication=_publication).delete()
        data = {
            'result': 2
        }
        return JsonResponse(data)