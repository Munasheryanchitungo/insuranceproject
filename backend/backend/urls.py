from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from . import views

def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        return HttpResponse("Superuser created")
    return HttpResponse("Superuser already exists")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('policies/', include('policies.urls')),
    path('policies/subscribe/', subscribe_policy, name='subscribe_policy'),
    path('claims/', include('claims.urls')),
    path('payments/', include('payments.urls')),
    path('help/', include('help.urls')),

    path('createsuperuser/', create_superuser),  # TEMPORARY
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
