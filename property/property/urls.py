from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('input/', include('input.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('admin1/', include('admin1.urls')),
     path('visualize/', include('visualization.urls'))
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
