# usuarios/domain/ports/output/user_repository.py

from abc import ABC, abstractmethod
from typing import Optional
from django.contrib.auth.models import User

class UserRepository(ABC):
    @abstractmethod
    def guardar_usuario(self, username: str, email: str, password: str) -> User:
        pass

    @abstractmethod
    def obtener_usuario_por_id(self, usuario_id: int) -> Optional[User]:
        pass

    def obtener_todos(self):
        pass

    @abstractmethod
    def actualizar_usuario(self, usuario: User) -> None:
        pass

    @abstractmethod
    def dar_de_baja_usuario(self, usuario_id: int) -> None:
        pass
