from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import *

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *


# class ContsctUsView(TemplateView):
    # template_name = 'contact_us/contact_us.html'


class ContactUsFormView(CreateView):
    model = contact_us
    template_name = 'contact_us/contact_us.html'
    fields = '__all__'
    success_url = 'contact-us'
    # context_object_name = 'form'





def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/contact-us/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "contact_us/contact_us.html", {"form": form})