# mi_app/application/services/departamento_service_impl.py

from typing import List

from departamentos.domain.entities import Departamento
from departamentos.domain.exception import DepartamentoError
from departamentos.domain.port.input import DepartamentoService
from departamentos.domain.port.output.departamento_repository import DepartamentoRepository


class DepartamentoServiceImpl(DepartamentoService):
    """Implementación de los casos de uso relacionados con Departamento."""

    def __init__(self, departamento_repository: DepartamentoRepository):
        self.departamento_repository = departamento_repository

    def crear_departamento(self, nombre: str) -> Departamento:
        """Crea un nuevo departamento y lo guarda en el repositorio."""
        if not nombre:
            raise DepartamentoError("El nombre del departamento no puede estar vacío.")

        # Crear la instancia de departamento
        departamento = Departamento(nombre=nombre)

        # Guardar usando el repositorio
        self.departamento_repository.guardar(departamento)

        return departamento

    def listar_departamentos(self) -> List[Departamento]:
        """Devuelve una lista de todos los departamentos."""
        # Obtener todos los departamentos usando el repositorio
        return self.departamento_repository.obtener_todos()

    def eliminar_departamento(self, nombre: str) -> None:
        """Elimina un departamento por su nombre."""
        if not nombre:
            raise DepartamentoError("El nombre del departamento no puede estar vacío.")

        # Eliminar el departamento usando el repositorio
        self.departamento_repository.eliminar(nombre)
