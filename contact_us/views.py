from django.views.generic.edit import CreateView
from .models import *
from django.shortcuts import render
from .forms import *



class ContactUsFormView(CreateView):
    form_class = ContactUsForm
    template_name = 'contact_us/contact_us.html'
    success_url = 'contact-us'






