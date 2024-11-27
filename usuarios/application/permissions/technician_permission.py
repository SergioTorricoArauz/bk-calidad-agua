# usuarios/infrastructure/permissions/technician_permission.py

from rest_framework.permissions import BasePermission


class IsTechnician(BasePermission):

    def has_permission(self, request, view):
        return (
                request.user
                and request.user.is_authenticated
                and request.user.groups.filter(name='Tecnico').exists()
        )
