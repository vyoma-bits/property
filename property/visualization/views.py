
from django.shortcuts import render,redirect
from input.models import Location
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Avg
from django.contrib.auth import authenticate,login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
# Create your views here.
def property1(request):
    properties=Location.objects.all()

    cities = list(properties.values_list('city', flat=True).distinct())
    property_counts = [properties.filter(city=city).count() for city in cities]
    
    micro_markets = list(properties.values_list('micro_market', flat=True).distinct())
    market_counts = [properties.filter(micro_market=micro_market).count() for micro_market in micro_markets]
    
    # Data for line graph (assuming you have a 'date' field)
    dates = list(properties.values_list('date', flat=True).distinct().order_by('date'))
    avg_prices = [properties.filter(date=date).aggregate(Avg('price_per_acre'))['price_per_acre__avg'] for date in dates]
    
    # Data for scatter plot
    parcel_sizes = list(properties.values_list('parcel_size', flat=True))
    prices_per_acre = list(properties.values_list('price_per_acre', flat=True))
    
    # Data for histogram
    property_sizes = list(properties.values_list('parcel_size', flat=True))
    
    context = {
        'cities': json.dumps(cities, cls=DjangoJSONEncoder),
        'property_counts': json.dumps(property_counts, cls=DjangoJSONEncoder),
        'micro_markets': json.dumps(micro_markets, cls=DjangoJSONEncoder),
        'market_counts': json.dumps(market_counts, cls=DjangoJSONEncoder),
        'dates': json.dumps(dates, cls=DjangoJSONEncoder),
        'avg_prices': json.dumps(avg_prices, cls=DjangoJSONEncoder),
        'parcel_sizes': json.dumps(parcel_sizes, cls=DjangoJSONEncoder),
        'prices_per_acre': json.dumps(prices_per_acre, cls=DjangoJSONEncoder),
        'property_sizes': json.dumps(property_sizes, cls=DjangoJSONEncoder),
    }
    return render(request, 'visualization/index.html', context)
from .filters import PropertyFilter
from django.core.serializers import serialize

def property_list(request):
    queryset = Location.objects.all()
    
    parcel_size_gt = request.GET.get('parcel_size_gt')
    if parcel_size_gt:
        queryset = queryset.filter(parcel_size__gt=float(parcel_size_gt))
    
    parcel_size_lt = request.GET.get('parcel_size_lt')
    if parcel_size_lt:
        queryset = queryset.filter(parcel_size__lt=float(parcel_size_lt))
    
    price_per_acre_gt = request.GET.get('price_per_acre_gt')
    if price_per_acre_gt:
        queryset = queryset.filter(price_per_acre__gt=float(price_per_acre_gt))
    
    price_per_acre_lt = request.GET.get('price_per_acre_lt')
    if price_per_acre_lt:
        queryset = queryset.filter(price_per_acre__lt=float(price_per_acre_lt))
    
    properties_json = serialize('json', queryset)
    return render(request, 'visualization/property_list.html', {'properties_json': properties_json})
