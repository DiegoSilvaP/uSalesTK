import django_filters
from .models import Publication, Category

class ProductFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Publication
        fields = ['product']

class CategoryFilter(django_filters.FilterSet):
    # product__category = django_filters.ChoiceFilter(lookup_expr='iexact')
    class Meta:
        model = Publication
        fields = ['product__category']