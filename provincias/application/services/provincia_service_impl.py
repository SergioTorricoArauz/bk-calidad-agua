# provincias/application/services/provincia_service_impl.py

from typing import List, Optional

from comunidades.domain.entities import Comunidad
from provincias.domain.entities import Provincia
from provincias.domain.exception import ProvinciaException
from provincias.domain.ports.input.provincia_service import ProvinciaService
from provincias.domain.ports.output.provincia_repository import ProvinciaRepository


class ProvinciaServiceImpl(ProvinciaService):
    def __init__(self, provincia_repository: ProvinciaRepository):
        self.provincia_repository = provincia_repository

    def crear_provincia(self, nombre: str, departamento_id: int) -> Provincia:
        provincia = Provincia(nombre=nombre, departamento_id=departamento_id)
        return self.provincia_repository.guardar(provincia)

    def listar_provincias(self) -> List[Provincia]:
        return self.provincia_repository.obtener_todas()

    def obtener_provincia_por_id(self, id: int) -> Optional[Provincia]:
        provincia = self.provincia_repository.obtener_por_id(id)
        if provincia is None:
            raise ProvinciaException(f"Provincia con id {id} no encontrada.")
        return provincia

    def eliminar_provincia(self, id: int) -> None:
        self.provincia_repository.eliminar(id)

    def actualizar_provincia(self, id: int, nombre: str, departamento_id: int) -> Provincia:
        provincia = self.obtener_provincia_por_id(id)
        provincia.nombre = nombre
        provincia.departamento_id = departamento_id
        return self.provincia_repository.actualizar(provincia)

    def listar_comunidades(self, provincia_id: int) -> list[Comunidad]:
        return self.provincia_repository.obtener_comunidades(provincia_id)
