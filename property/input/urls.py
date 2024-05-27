from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store_info/', views.store_info, name='store_info'),
]
