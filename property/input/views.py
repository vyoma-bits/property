from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import LocationForm,BrokerForm
import json
from django.urls import reverse
from . models import Location
import requests
from django.core.files.base import ContentFile

def index(request):
    form = LocationForm()

    return render(request, 'user/index.html', {'form': form})



def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return ContentFile(response.content)
    return None

def store_info(request):

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            photo_url = form.cleaned_data.get('photo_url')
            propertyid=form.cleaned_data.get('property_id')
            if photo_url:
                image_content = download_image(photo_url)
                if image_content:
                    location.photo.save(f"{location.location}.jpg", image_content)
            location.save()
            url = reverse('broker', kwargs={'propertyid': propertyid})
            return redirect(url)
    else:
        form = LocationForm()
    
    return render(request, 'input/index.html', {'form': form})
def success(request):
    return render(request,"input/success.html")
def add_marker(request):
    location = Location.objects.all()
    locations_data = json.dumps([
        {
            'location': loc.location,
            'latitude': loc.latitude,
            'longitude': loc.longitude,
            'parcel_size': int(loc.parcel_size),
            'price_per_acre': int(loc.price_per_acre),
            'micro_market': loc.micro_market,
            'city': loc.city,
            'photo_url': loc.photo.url if loc.photo else ''
        } for loc in location
    ])
    return render(request,"input/index2.html",{'location':locations_data})
def datables(request):
    return render(request,"input/datatables.html")
def broker_form(request,propertyid):
    submitted=False
    property1=Location.objects.get(property_id=propertyid)
    if request.method == "POST":
        form=BrokerForm(request.POST,initial={'propertyid':property1})
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=BrokerForm(request.POST,initial={'propertyid':property1})
        if 'submitted' in request.GET:
            submitted=request.GET.get('submitted')
    return render(request,'input/broker_form.html',{'form':form,'submitted':submitted})

