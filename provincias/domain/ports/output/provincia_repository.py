# provincias/domain/ports/output/provincia_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from provincias.domain.entities import Provincia


class ProvinciaRepository(ABC):
    @abstractmethod
    def guardar(self, provincia: Provincia) -> Provincia:
        """Guarda una provincia y devuelve la entidad con el ID asignado."""
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Provincia]:
        """Devuelve una provincia por su ID si existe."""
        pass

    @abstractmethod
    def obtener_por_nombre(self, nombre: str) -> Optional[Provincia]:
        """Devuelve una provincia por su nombre si existe."""
        pass

    @abstractmethod
    def obtener_por_departamento_id(self, departamento_id: int) -> List[Provincia]:
        """Devuelve todas las provincias de un departamento específico."""
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        """Elimina una provincia por su ID."""
        pass

    @abstractmethod
    def obtener_todas(self) -> List[Provincia]:
        """Devuelve una lista de todas las provincias."""
        pass

    def actualizar(self, provincia):
        """Actualiza una provincia existente en la base de datos."""
        pass
