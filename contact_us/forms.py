
from django import forms
from django.forms import ModelForm
from .models import *




class ContactUsForm(ModelForm):
    class Meta:
        model = contact_us
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': "w-100 form-control border-0 py-3 mb-4" , 'placeholder':"Your Name"}),
            'email': forms.TextInput(attrs={'class': "w-100 form-control border-0 py-3 mb-4", 'placeholder':"Enter Your Email"}),
            'phone': forms.TextInput(attrs={'class': "w-100 form-control border-0 py-3 mb-4", 'placeholder':"Your Phone"}),
            'message': forms.Textarea(attrs={'class': "w-100 form-control border-0 mb-4", 'placeholder':"Your Message"}),
        }

        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'message': '',            
        }