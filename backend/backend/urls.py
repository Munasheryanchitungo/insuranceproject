from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('policies/', include('backend.policies.urls')),
    path('claims/', include('backend.claims.urls')),
    path('payments/', include('backend.payments.urls')),
    path('help/', include('backend.help.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)