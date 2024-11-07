from django.urls import path, include
from rest_framework import routers

from departamentos.infrastructure.views import DepartamentoViewSet

router = routers.DefaultRouter()
router.register(r'departamento', DepartamentoViewSet, basename='departamento')

urlpatterns = [
    path('', include(router.urls)),
]
