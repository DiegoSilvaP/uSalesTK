from django.views.generic.list import ListView
from django.views.generic import View
from .models import Shopping_basketItem
from publications.models import Publication
from django.http import JsonResponse
from django.contrib.auth.models import User
from information.models import AboutUs
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
@method_decorator(login_required, name='dispatch')
class Shopping_basketListView(ListView):
    model = Shopping_basketItem
    def get_context_data(self, **kwargs):
        context = super(Shopping_basketListView, self).get_context_data(**kwargs)
        context['aboutus'] = AboutUs.objects.first()
        if self.request.user.is_anonymous !=True:
            context['publications'] = Publication.objects.all()
            # context['basket_list'] = Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
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
