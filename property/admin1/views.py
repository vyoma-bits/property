from django.shortcuts import render,redirect,HttpResponseRedirect
import json
from django.urls import reverse
from input.models import Location
from user.models import enquiry
from input.models import Broker
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
from django.core.files.base import ContentFile
@login_required(login_url='/user/loginc')
# Create your views here.
def home(request):
    properties=Location.objects.all()
    context={'properties':properties}
    enquiries=enquiry.objects.all()
    context={'properties':properties,'enquiries':enquiries}
    return render(request,"admin1/home/index.html",context)

def allProperties(request):
    properties=Location.objects.all()
    context={'properties':properties}
    return render(request,"admin1/home/notifications.html",context)
@login_required(login_url='/user/loginc')
def property1(request,propertyid):
    loc = Location.objects.get(property_id=propertyid)
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
        } 
    ])
    return render(request,"admin1/home/login.html",{'location':locations_data})
@login_required(login_url='/user/loginc')
def enquiries(request):
    enquiries=enquiry.objects.all()
    context={'enquiries':enquiries}
    return render(request,"admin1/home/register.html",context)
@login_required(login_url='/user/loginc')
def brokers(request):
    brokers=Broker.objects.all()
    context={'brokers':brokers}
    print(brokers)
    return render(request,"admin1/home/page-404.html",context)
def user(request):
    user=User.objects.get(username=request.user.username)
    return render(request,"admin1/home/user.html",{"user":user})
    


