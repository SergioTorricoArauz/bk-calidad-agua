from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from usuarios.infrastructure.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet, basename='usuario')
urlpatterns = [
    path('', include(router.urls)),
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
