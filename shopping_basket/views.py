from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import View
from .models import Shopping_basketItem
from wish_list.models import Wish_listItem
from publications.models import Publication
from django.http import JsonResponse
from django.contrib.auth.models import User


class Shopping_basketItemAdd(View):
    def get(self, request, *args, **kwargs):
        _quantity = request.GET['cantidad']
        _publication = Publication.objects.get(id=request.GET['producto'])
        _customer = self.request.user
        _price = _publication.price
        subtotal = float(_price)*int(_quantity)
        Shopping_basketItem(customer = _customer,publication=_publication, quantity = _quantity, price = _price).save()
        data = {
            'quantity':_quantity,
            'price':subtotal
        }
        return JsonResponse(data)

class Shopping_basketItemUpdate(View):
    def get(self, request, *args, **kwargs):
        _quantity = request.GET['cantidad']
        _publication = Publication.objects.get(id=request.GET['producto'])
        _customer = self.request.user.id
        _price = _publication.price
        subtotal = float(_price)*int(_quantity)
        Shopping_basketItem.objects.filter(customer = _customer,publication=_publication).update(quantity = int(_quantity), price= subtotal)
        data = {
            'quantity':_quantity,
            'price':subtotal
        }
        return JsonResponse(data)


# Create your views here.
class Shopping_basketListView(ListView):
    model = Shopping_basketItem

    def get_context_data(self, **kwargs):
        context = super(Shopping_basketListView, self).get_context_data(**kwargs)
        context['wish_list'] = Wish_listItem.objects.filter(customer=self.request.user).values_list("publication").values()
        if self.request.user.is_anonymous !=True:
            context['publications'] = Publication.objects.all().values_list("product").values()
        return context

class Shopping_basketItemDelete(View):
    def get(self, request, *args, **kwargs):
        _publication = Publication.objects.get(id=request.GET['producto'])
        _customer = self.request.user.id
        Shopping_basketItem.objects.filter(customer = _customer,publication=_publication).delete()
        
        data = {
            'result':1
        }
        return JsonResponse(data)
