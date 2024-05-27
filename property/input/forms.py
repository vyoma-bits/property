# In forms.py inside the maps app directory
from django import forms

class InfoForm(forms.Form):
    location = forms.CharField(label='Location')
