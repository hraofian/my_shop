
from django.urls import path
from . import  views

urlpatterns = [
    # path('', views.ContsctUsView.as_view(), name='contact-us'),  
    path('', views.ContactUsFormView.as_view(), name='contact-us'),  
    # path('', views.get_name, name='contact-us'),  

]
 