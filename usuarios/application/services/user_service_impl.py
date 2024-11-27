# usuarios/application/services/user_service_impl.py

from django.contrib.auth.models import User, Group
from usuarios.domain.ports.input.user_service import UserService


class UserServiceImpl(UserService):
    def crear_usuario(self, username: str, email: str, password: str, grupo_nombre: str) -> User:
        usuario = User.objects.create_user(username=username, email=email, password=password)

        grupo = Group.objects.get(name=grupo_nombre)
        usuario.groups.add(grupo)

        return usuario

    def obtener_usuario_por_id(self, usuario_id: int) -> User:
        return User.objects.get(id=usuario_id)

    def asignar_rol(self, usuario_id: int, grupo_nombre: str) -> None:
        usuario = User.objects.get(id=usuario_id)
        grupo = Group.objects.get(name=grupo_nombre)
        usuario.groups.clear()  # Opcional: limpiar otros grupos antes de asignar uno nuevo
        usuario.groups.add(grupo)

    def editar_usuario(self, usuario_id: int, **datos) -> User:
        usuario = User.objects.get(id=usuario_id)
        for key, value in datos.items():
            setattr(usuario, key, value)
        usuario.save()
        return usuario

    def dar_de_baja_usuario(self, usuario_id: int) -> None:
        usuario = User.objects.get(id=usuario_id)
        usuario.is_active = False
        usuario.save()
