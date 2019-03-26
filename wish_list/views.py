from .models import Wish_listItem
from publications.models import Publication
from django.views.generic.list import ListView
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Wish_listListView(ListView):
    model = Wish_listItem


class Wish_listAdd(View):
    def get(self, request, *args, **kwargs):
        publication = request.GET['publication']
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
        _publication = Publication.objects.get(id=publication)
        _customer = self.request.user
        Wish_listItem.objects.get(customer = _customer,publication=_publication).delete()
        data = {
            'result': 2
        }
        return JsonResponse(data)