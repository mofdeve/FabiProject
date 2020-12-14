from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('shop/', include('shop.urls')),
    path('service/', include('service.urls')),
]
