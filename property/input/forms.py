from django import forms
from .models import Location,Broker

class LocationForm(forms.ModelForm):
    photo_url = forms.URLField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Location
        fields = ['location', 'latitude', 'longitude', 'parcel_size', 'price_per_acre', 'micro_market', 'city','property_id']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
class BrokerForm(forms.ModelForm):
    class Meta:
        model=Broker
        fields="__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the username instance (assuming it's pre-populated)
        if 'initial' in kwargs and 'propertyid' in kwargs['initial']:
            username_instance = kwargs['initial']['propertyid']
        else:
            # Handle the case where initial value is not provided
            username_instance = None  # Or set a default username instance

        # Make the username field read-only
        self.fields['property_id'].widget = forms.widgets.Select(choices=[(username_instance.pk, str(username_instance))])
      
