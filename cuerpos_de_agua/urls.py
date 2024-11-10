from rest_framework import routers

from cuerpos_de_agua.infrastructure.views import CuerpoDeAguaViewSet

router = routers.DefaultRouter()

router.register(r'cuerpos_de_agua', CuerpoDeAguaViewSet, basename='cuerpos_de_agua')

urlpatterns = router.urls
