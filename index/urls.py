
from django.urls import path
from . import  views

urlpatterns = [
    # path('', IndexView.as_view() , name='index' ),
    path('', views.members , name='members' ),
    path('details/<int:id>', views.details, name='details'),


]
