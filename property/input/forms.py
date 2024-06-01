from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    photo_url = forms.URLField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Location
        fields = ['location', 'latitude', 'longitude', 'parcel_size', 'price_per_acre', 'micro_market', 'city','photo']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
