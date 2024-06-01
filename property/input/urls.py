from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [

    path('store_info/', views.store_info, name='store_info'),
     path('success/', views.success, name='success_page'),
     path('marker/',views.add_marker,name="marker")
]
