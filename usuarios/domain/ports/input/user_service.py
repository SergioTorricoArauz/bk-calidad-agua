# usuarios/domain/ports/input/user_service.py

from abc import ABC, abstractmethod
from django.contrib.auth.models import User

class UserService(ABC):
    @abstractmethod
    def crear_usuario(self, username: str, email: str, password: str, grupo_nombre: str) -> User:
        pass

    @abstractmethod
    def obtener_usuario_por_id(self, usuario_id: int) -> User:
        pass

    def obtener_todos(self):
        pass

    @abstractmethod
    def asignar_rol(self, usuario_id: int, grupo_nombre: str) -> None:
        pass

    @abstractmethod
    def editar_usuario(self, usuario_id: int, **datos) -> User:
        pass

    @abstractmethod
    def dar_de_baja_usuario(self, usuario_id: int) -> None:
        pass
