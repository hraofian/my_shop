
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=300 , label='your name',disabled=False)

