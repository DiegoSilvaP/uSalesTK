from django.views.generic.base import TemplateView
from wish_list.models import Wish_listItem

class HomePageView(TemplateView):

    template_name = "core/home.html"
    