# mi_app/domain/ports/input/departamento_service.py

from abc import ABC, abstractmethod
from typing import List, Optional

from departamentos.domain.entities import Departamento


class DepartamentoService(ABC):
    """Define el puerto de entrada para los casos de uso relacionados con los departamentos."""

    @abstractmethod
    def crear_departamento(self, nombre: str) -> Departamento:
        """Crea un nuevo departamento en el sistema."""
        pass

    @abstractmethod
    def listar_departamentos(self) -> List[Departamento]:
        """Devuelve una lista de todos los departamentos."""
        pass

    @abstractmethod
    def obtener_departamento_por_id(self, id: int) -> Optional[Departamento]:
        """Devuelve un departamento por su ID, si existe."""
        pass

    @abstractmethod
    def eliminar_departamento(self, nombre: str) -> None:
        """Elimina un departamento por su nombre."""
        pass
