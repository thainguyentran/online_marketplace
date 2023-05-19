from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('items/', include('item.urls')),
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
