from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import *



class ShopView(TemplateView):
    template_name = 'shop/shop.html'


class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'product'