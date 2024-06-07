from .models import enquiry
from django import forms
class enquiryForm(forms.ModelForm):
    class Meta:
        model=enquiry
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