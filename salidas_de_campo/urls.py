from django.urls import include, path
from rest_framework import routers

from salidas_de_campo.infrastructure.views import SalidaDeCampoViewSet

router = routers.DefaultRouter()
router.register(r'salidas_de_campo', SalidaDeCampoViewSet, basename='salidas_de_campo')

urlpatterns = [
    path('', include(router.urls)),
]
