# mi_app/domain/ports/output/departamento_repository.py

from abc import ABC, abstractmethod
from typing import Optional, List
from departamentos.domain.entities import Departamento


class DepartamentoRepository(ABC):
    """Interfaz para el repositorio de Departamento"""

    @abstractmethod
    def guardar(self, departamento: Departamento) -> Departamento:
        """Guarda un departamento y devuelve la entidad con el ID asignado."""
        pass

    @abstractmethod
    def obtener_por_nombre(self, nombre: str) -> Optional[Departamento]:
        """Busca un departamento por su nombre y lo devuelve si existe."""
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Departamento]:
        """Busca un departamento por su ID y lo devuelve si existe."""
        pass

    @abstractmethod
    def eliminar(self, nombre: str) -> None:
        """Elimina un departamento por nombre."""
        pass

    @abstractmethod
    def eliminar_por_id(self, id: int) -> None:
        """Elimina un departamento por su ID."""
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Departamento]:
        """Devuelve una lista de todos los departamentos."""
        pass
