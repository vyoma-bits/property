from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
path('',views.index,name="datatables"),
    path('store_info/', views.store_info, name='store_info'),
     path('success/', views.success, name='success_page'),
     path('marker/',views.add_marker,name="marker"),
     path('datatables/',views.datables,name="datatables"),
    path('broker/<int:propertyid>',views.broker_form,name="broker")
]
