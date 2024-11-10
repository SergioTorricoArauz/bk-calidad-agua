# cuerpos_de_agua/application/services/cuerpo_de_agua_service_impl.py

from typing import List, Optional
from cuerpos_de_agua.domain.entities.cuerpo_de_agua import CuerpoDeAgua
from cuerpos_de_agua.domain.exception.cuerpo_de_agua_exception import CuerpoDeAguaException
from cuerpos_de_agua.domain.ports.input.cuerpo_de_agua_service import CuerpoDeAguaService
from cuerpos_de_agua.domain.ports.output.cuerpo_de_agua_repository import CuerpoDeAguaRepository


class CuerpoDeAguaServiceImpl(CuerpoDeAguaService):

    def __init__(self, cuerpo_de_agua_repository: CuerpoDeAguaRepository):
        self.cuerpo_de_agua_repository = cuerpo_de_agua_repository

    def crear_cuerpo_de_agua(self, nombre: str, tipo: str, latitud: Optional[float], longitud: Optional[float],
                             comunidad_id: int) -> CuerpoDeAgua:
        if not nombre or not tipo or not comunidad_id:
            raise CuerpoDeAguaException("Nombre, tipo y comunidad_id son campos obligatorios.")

        cuerpo_de_agua = CuerpoDeAgua(nombre=nombre, tipo=tipo, latitud=latitud, longitud=longitud,
                                      comunidad_id=comunidad_id)

        return self.cuerpo_de_agua_repository.guardar(cuerpo_de_agua)

    def listar_cuerpos_de_agua(self) -> List[CuerpoDeAgua]:
        return self.cuerpo_de_agua_repository.obtener_todos()

    def obtener_cuerpo_de_agua_por_id(self, id: int) -> Optional[CuerpoDeAgua]:
        cuerpo_de_agua = self.cuerpo_de_agua_repository.obtener_por_id(id)
        if cuerpo_de_agua is None:
            raise CuerpoDeAguaException(f"Cuerpo de agua con ID {id} no encontrado.")
        return cuerpo_de_agua

    def eliminar_cuerpo_de_agua(self, id: int) -> None:
        cuerpo_de_agua = self.obtener_cuerpo_de_agua_por_id(id)
        if cuerpo_de_agua is None:
            raise CuerpoDeAguaException(f"No se puede eliminar: Cuerpo de agua con ID {id} no encontrado.")

        self.cuerpo_de_agua_repository.eliminar(id)

    def actualizar_cuerpo_de_agua(self, cuerpo_de_agua: CuerpoDeAgua) -> CuerpoDeAgua:
        pass


