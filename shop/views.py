from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import *
from django.views.generic.detail import DetailView



class ShopView(TemplateView):
    template_name = 'shop/shop.html'


class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'product'
    paginate_by = 9


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/shop_detail.html'
    context_object_name = 'product_detail'