from django.urls import path, include
from rest_framework import routers

from analisis_muestreo.infrastructure.views import AnalisisTurbidezViewSet, AnalisisCaudalViewSet

router = routers.DefaultRouter()

router.register('analisis-turbidez', AnalisisTurbidezViewSet, basename='analisis-turbidez')
router.register('analisis_caudal', AnalisisCaudalViewSet, basename='analisis-caudal')

urlpatterns = [
    path('', include(router.urls)),
]
