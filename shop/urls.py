
from django.urls import path
from . import  views

urlpatterns = [
    # path('', views.ShopView.as_view(), name='shop'),   
    path('', views.ProductListView.as_view(), name='shop'),   
    path('<slug:slug>', views.ProductDetailView.as_view(), name='shop_detail'),   
]

