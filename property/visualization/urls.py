from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path("",views.property1,name="index"),
    path('properties/', views.property_list, name='property_list'),

    
   
]
