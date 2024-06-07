from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index,name="home2"),
    path("loginc",views.loginc,name="login"),
    path("enquiry/<int:propertyid>",views.enquiry,name="enquiry"),
    path("logout",views.logout1,name="logout"),
    
   
]
