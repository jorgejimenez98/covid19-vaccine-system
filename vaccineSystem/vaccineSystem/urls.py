from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Apps URLS
    path("", include("apps.main.urls")),
    path("", include("apps.users.urls")),
    path("", include("apps.locality.urls")),
    path("", include("apps.vaccine.urls")),
]

if settings.DEBUG:  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)