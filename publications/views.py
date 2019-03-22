from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Publication, Category
from .filters import ProductFilter
from .forms import PublicationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.defaultfilters import slugify
from carousel.models import Carousel
# Proteger vistas de usuarios no logueados
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Create your views here.
class PublicationListSearchView(ListView):
    model = Publication
    def get_context_data(self, **kwargs):
        context = super(PublicationListSearchView, self).get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PublicationListView(ListView):
    model = Publication
    def get_context_data(self, **kwargs):
        context = super(PublicationListView, self).get_context_data(**kwargs)
        context['carousel'] = Carousel.objects.all()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context
        
class PublicationDetailView(DetailView):
    model = Publication

@method_decorator(staff_member_required, name='dispatch')
class PublicationCreate(CreateView):
    model = Publication
    form_class = PublicationForm
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
    def get_success_url(self):
        return reverse_lazy('publications:publication', args=[self.object.id, slugify(self.object.product)])


@method_decorator(staff_member_required, name='dispatch')
class PublicationDelete(DeleteView):
    model = Publication
    success_url = reverse_lazy('publications:publications')
