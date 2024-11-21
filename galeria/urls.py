from django.urls import path, include
from rest_framework import routers

from galeria.infrastructure.views import ImagenViewSet

router = routers.DefaultRouter()

router.register('galeria', ImagenViewSet, basename='galeria')

urlpatterns = [
    path('', include(router.urls)),
]
