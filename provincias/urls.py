from django.urls import path, include
from rest_framework import routers

from provincias.infrastructure.views import ProvinciaViewSet

router = routers.DefaultRouter()

router.register(r'provincias', ProvinciaViewSet, basename='provincias')
urlpatterns = [
    path('', include(router.urls)),
]
