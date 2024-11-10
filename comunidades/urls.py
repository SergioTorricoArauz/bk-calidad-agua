from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from comunidades.infrastructure.views import ComunidadViewSet

router = routers.DefaultRouter()

router.register(r'comunidades', ComunidadViewSet, basename='comunidades')

urlpatterns = router.urls
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
