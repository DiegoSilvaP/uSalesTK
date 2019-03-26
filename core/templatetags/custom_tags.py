from django import template
from publications.models import Publication
from wish_list.models import Wish_listItem
from shopping_basket.models import Shopping_basketItem
from publications.models import Category, SubCategory
from information.models import AboutUs, Privacy, FAQ
from orders.models import Orders

# from privacyPolicy.models import Privacy
# from faq.models import FAQ
from django.db.models import Sum


register = template.Library()

@register.filter
def wishlist_counter(usuario, id):
    return Wish_listItem.objects.filter(customer=id).count()

@register.simple_tag
def publications():
    return Publication.objects.all()

@register.filter
def basketlist_counter(usuario, id):
    # qty=0
    # for q in Shopping_basketItem.objects.filter(customer=id):
        # qty+=q.quantity
    return Shopping_basketItem.objects.filter(customer=id).aggregate(Sum('quantity'))['quantity__sum']


@register.simple_tag(takes_context=True)
def wish_list(context):
    return Wish_listItem.objects.filter(customer=context['user'].id).values_list("publication").values()


@register.simple_tag(takes_context=True)
def orders_list(context):
    return Orders.objects.filter(customer=context['user'].id)

@register.simple_tag(takes_context=True)
def basket_list(context):
    return Shopping_basketItem.objects.filter(customer=context['user'].id).values_list("publication").values()

@register.simple_tag
def categories():
    return Category.objects.all()

@register.simple_tag
def subCategories():
    return SubCategory.objects.all()

@register.simple_tag
def aboutus():
    return AboutUs.objects.first()

@register.simple_tag
def privacy():
    return Privacy.objects.first()

@register.simple_tag
def faq():
    return FAQ.objects.all()