from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from django_project_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
