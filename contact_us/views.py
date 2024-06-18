from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import *

# class ContsctUsView(TemplateView):
    # template_name = 'contact_us/contact_us.html'


class ContactUsFormView(CreateView):
    model = contact_us
    template_name = 'contact_us/contact_us.html'
    fields = '__all__'
    success_url = 'contact-us'