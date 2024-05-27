from django.shortcuts import render
from .forms import InfoForm
import json

def index(request):
    form = InfoForm()
    return render(request, 'input/index.html', {'form': form})



def store_info(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            latitude = request.POST.get('latitude')  # Get latitude from form data
            longitude = request.POST.get('longitude')  # Get longitude from form data

            # Retrieve image of the location from Google Maps API
         

            # Store location, latitude, longitude, and image URL in the database or perform any other desired action
            return render(request, 'input/success.html', {'location': location, 'latitude': latitude, 'longitude': longitude})
    else:
        form = InfoForm()
    return render(request, 'input/index.html', {'form': form})
