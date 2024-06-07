from django.shortcuts import render,redirect
from input.models import Location
def index(request):

    return render(request,"dashboard/graphs.html")
