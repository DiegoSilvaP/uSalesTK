from django.shortcuts import render, resolve_url, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views import View
from .models import Orders
from publications.models import Publication
from shopping_basket.models import Shopping_basketItem
from django.http import JsonResponse
import datetime
from random import randint

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class OrdersListView(ListView):
    model = Orders

class OrderCreate(View):
    def get(self, request, *args, **kwargs):
        _customer = self.request.user
        _product=self.request.GET['publication']
        _quantity=self.request.GET['quantity']
        _subtotal=self.request.GET['subtotal']
        _folio = datetime.datetime.now().strftime("%y%m%d%H%M%S")+str(randint(1000, 9999))
        _publication = Publication.objects.get(id=_product)
        _newPublicationStock = _publication.stock-int(_quantity)
        Orders(folio=_folio, customer=_customer,product=_publication,quantity=_quantity,subtotal=_subtotal).save()
        Shopping_basketItem.objects.get(customer = _customer,publication=_publication).delete()
        Publication.objects.filter(id = _product).update(stock = _newPublicationStock)
        data = {
            'result':1
        }
        return JsonResponse(data)
        

