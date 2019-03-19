from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Publication, Category
from .filters import ProductFilter, CategoryFilter
from .forms import PublicationForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

from wish_list.models import Wish_listItem


# Proteger vistas de usuarios no logueados
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView

from shopping_basket.models import Shopping_basketItem


# Create your views here.
# class PublicationListView(ListView):

class PublicationListSearchView(ListView):
    model = Publication
    def get_context_data(self, **kwargs):
        context = super(PublicationListSearchView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        # context['filterCategory'] = CategoryFilter(self.request.GET, queryset=self.get_queryset())
        if self.request.user.is_anonymous !=True:
            context['wish_list'] = Wish_listItem.objects.filter(customer=self.request.user).values_list("publication").values()
            context['basket_list'] = Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            qty=0
            for q in Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("quantity").values():
                qty += q['quantity']
            context['basket_quantity'] = qty
        return context

class PublicationListView(ListView):
    model = Publication
    def get_context_data(self, **kwargs):
        context = super(PublicationListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        # context['filterCategory'] = CategoryFilter(self.request.GET, queryset=self.get_queryset())
        if self.request.user.is_anonymous !=True:
            context['wish_list'] = Wish_listItem.objects.filter(customer=self.request.user).values_list("publication").values()
            context['basket_list'] = Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            qty=0
            for q in Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("quantity").values():
                qty += q['quantity']
            context['basket_quantity'] = qty
        return context
        
class PublicationDetailView(DetailView):
    model = Publication
    def get_context_data(self, *args, **kwargs):
        
        context = super(PublicationDetailView, self).get_context_data(**kwargs)
        print(self.request)
        if self.request.user.is_anonymous !=True:
            context['wish_list'] = Wish_listItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            context['basket_list'] = Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            qty=0
            for q in Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("quantity").values():
                qty += q['quantity']
            context['basket_quantity'] = qty
        return context

@method_decorator(staff_member_required, name='dispatch')
class PublicationCreate(CreateView):
    model = Publication
    form_class = PublicationForm
    def get_context_data(self, **kwargs):
        context = super(PublicationCreate, self).get_context_data(**kwargs)
        if self.request.user.is_anonymous !=True:
            context['wish_list'] = Wish_listItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            context['basket_list'] = Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            qty=0
            for q in Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("quantity").values():
                qty += q['quantity']
            context['basket_quantity'] = qty
        return context

    # Sobreescribimos el metodo get_success_url para que nos redirija automaticamente a la publicacion creada por medio del ID y del SLUG
    def get_success_url(self):
        # print("ID:",self.object.id, "Slug:",slugify(self.object.name))
        return reverse_lazy('publications:publication', args=[self.object.id, slugify(self.object.product)])

@method_decorator(staff_member_required, name='dispatch')
class PublicationUpdate(UpdateView):
    model = Publication
    form_class = PublicationForm
    # El sufijo se establece, para que vaya a buscar el template, de lo contrario iria a buscar el template de creacion
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        context = super(PublicationUpdate, self).get_context_data(**kwargs)
        if self.request.user.is_anonymous !=True:
            context['wish_list'] = Wish_listItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            context['basket_list'] = Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            qty=0
            for q in Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("quantity").values():
                qty += q['quantity']
            context['basket_quantity'] = qty
        return context

    def get_success_url(self):
        return reverse_lazy('publications:publication', args=[self.object.id, slugify(self.object.product)])


@method_decorator(staff_member_required, name='dispatch')
class PublicationDelete(DeleteView):
    model = Publication
    success_url = reverse_lazy('publications:publications')

    def get_context_data(self, **kwargs):
        context = super(PublicationDelete, self).get_context_data(**kwargs)
        if self.request.user.is_anonymous !=True:
            context['wish_list'] = Wish_listItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            context['basket_list'] = Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("publication").values()
            qty=0
            for q in Shopping_basketItem.objects.filter(customer=self.request.user.id).values_list("quantity").values():
                qty += q['quantity']
            context['basket_quantity'] = qty
        return context
