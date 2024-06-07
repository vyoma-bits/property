from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns=[
    path("dashboard",views.home,name="home"),
    path("property/<int:propertyid>",views.property1,name="property"),
    path("allproperty",views.allProperties,name="all"),
    path("enquiries",views.enquiries,name="allenquiry"),
     path("brokers",views.brokers,name="allbroker"),
     path("user",views.user,name="user"),




]