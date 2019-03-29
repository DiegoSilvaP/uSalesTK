from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views import View
from .models import Orders
from publications.models import Publication
from shopping_basket.models import Shopping_basketItem
from django.http import JsonResponse
import datetime
from random import randint
from .forms import OrderForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class OrdersListView(ListView):
    model = Orders

# class OrderCreate(CreateView):
#     model = Orders
#     form_class = OrderForm
#     success_url = reverse_lazy('orders:orders')

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

class OrderUpdate(UpdateView):
    model = Orders
    form_class = OrderForm
    template_name_suffix = '_update_form'
    # template_name = 'orders/order-finish_purchase.html'
    def get_success_url(self):
        return  reverse_lazy('orders:orders') + '?success'
        

