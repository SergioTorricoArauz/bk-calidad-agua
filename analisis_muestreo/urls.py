from django.urls import path, include
from rest_framework import routers

from analisis_muestreo.infrastructure.views import AnalisisView
from analisis_muestreo.infrastructure.views.analisis_view import AnalisisDetailView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path("analisis/", AnalisisView.as_view(), name="crear_analisis"),  # Crear y listar análisis
    path("analisis/<int:id>/", AnalisisDetailView.as_view(), name="detalle_analisis"),
    # Ver detalles y eliminar análisis
]
