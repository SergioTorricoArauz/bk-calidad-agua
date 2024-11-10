# comunidades/application/services/comunidad_service_impl.py

from typing import List, Optional
from comunidades.domain.entities.comunidad import Comunidad
from comunidades.domain.exception.comunidad_exception import ComunidadException
from comunidades.domain.ports.input.comunidad_service import ComunidadService
from comunidades.domain.ports.output.comunidad_repository import ComunidadRepository
from cuerpos_de_agua.domain.entities import CuerpoDeAgua


class ComunidadServiceImpl(ComunidadService):
    def __init__(self, comunidad_repository: ComunidadRepository):
        self.comunidad_repository = comunidad_repository

    def crear_comunidad(self, nombre: str, provincia_id: int) -> Comunidad:
        if not nombre or not provincia_id:
            raise ComunidadException("Nombre y provincia_id son campos obligatorios.")
        comunidad = Comunidad(nombre=nombre, provincia_id=provincia_id)
        return self.comunidad_repository.guardar(comunidad)

    def listar_comunidades(self) -> List[Comunidad]:
        return self.comunidad_repository.obtener_todas()

    def obtener_comunidad_por_id(self, id: int) -> Optional[Comunidad]:
        comunidad = self.comunidad_repository.obtener_por_id(id)
        if comunidad is None:
            raise ComunidadException(f"Comunidad con ID {id} no encontrada.")
        return comunidad

    def eliminar_comunidad(self, id: int) -> None:
        comunidad = self.obtener_comunidad_por_id(id)
        if comunidad is None:
            raise ComunidadException(f"No se puede eliminar: Comunidad con ID {id} no encontrada.")
        self.comunidad_repository.eliminar(id)

    def actualizar_comunidad(self, id: int, nombre: str, provincia_id: int) -> Comunidad:
        comunidad = self.obtener_comunidad_por_id(id)
        if not comunidad:
            raise ComunidadException(f"Comunidad con ID {id} no encontrada.")

        comunidad.nombre = nombre
        comunidad.provincia_id = provincia_id
        return self.comunidad_repository.actualizar(comunidad)

    def obtener_cuerpos_de_agua(self, comunidad_id: int) -> List[CuerpoDeAgua]:
        return self.comunidad_repository.obtener_cuerpos_de_agua(comunidad_id)
