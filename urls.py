from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', include('cms.urls')),
    path('api/docs/', include_docs_urls(title='MiNi CMS API Docs')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.FORCE_STATIC_FILE_SERVING and not settings.DEBUG:
    settings.DEBUG = True
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    settings.DEBUG = False
