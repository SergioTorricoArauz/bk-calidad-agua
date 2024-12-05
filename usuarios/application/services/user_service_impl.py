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

    def obtener_todos(self):
        return User.objects.all()

    def asignar_rol(self, usuario_id: int, grupo_nombre: str) -> None:
        usuario = User.objects.get(id=usuario_id)
        grupo = Group.objects.get(name=grupo_nombre)
        usuario.groups.clear()  # Opcional: limpiar otros grupos antes de asignar uno nuevo
        usuario.groups.add(grupo)

    # usuarios/application/services/user_service_impl.py

    def editar_usuario(self, usuario_id: int, **datos) -> User:
        usuario = User.objects.get(id=usuario_id)
        grupo_nombre = datos.pop('grupo', None)  # Extract the group name if provided

        for key, value in datos.items():
            setattr(usuario, key, value)

        usuario.save()

        if grupo_nombre:
            grupo = Group.objects.get(name=grupo_nombre)
            usuario.groups.clear()  # Clear existing groups
            usuario.groups.add(grupo)  # Assign the new group

        return usuario

    def dar_de_baja_usuario(self, usuario_id: int) -> None:
        usuario = User.objects.get(id=usuario_id)
        usuario.is_active = False
        usuario.save()
