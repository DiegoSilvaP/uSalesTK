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
        # print('en multiple')
        # print(self.request.user)
        
        publicationContext = context = super(Wish_listListView, self).get_context_data(**kwargs)
        if self.request.user.is_anonymous !=True:
            context['publications'] = Publication.objects.all().values_list("product").values()
            # wishContext = context['wishlist']
            # print('publication context',publicationContext.values())
        return context


class Wish_listAdd(View):
    # print('agregando producto a la wishlist')
    def get(self, request, *args, **kwargs):
        publication = request.GET['publication']
        customer = request.GET['customer']
        _publication = Publication.objects.get(id=publication)
        _customer = User.objects.get(id=customer)
        Wish_listItem(customer = _customer,publication=_publication).save()
        data = {
            'result': 1
        }
        # return HttpResponseRedirect('/your_success_url/')
        return JsonResponse(data)

class Wish_listDelete(View):
    # print('eliminando producto a la wishlist')
    def get(self, request, *args, **kwargs):
        publication = request.GET['publication']
        customer = request.GET['customer']

        _publication = Publication.objects.get(id=publication)
        _customer = User.objects.get(id=customer)

        # print("para borrar ",_publication,_customer)
        my_obj = Wish_listItem.objects.get(customer = _customer,publication=_publication)
        my_obj.delete()
        data = {
            'result': 2
        }
        # return HttpResponseRedirect('/your_success_url/')
        return JsonResponse(data)