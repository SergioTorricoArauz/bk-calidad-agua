# salidas_de_campo/domain/ports/input/salida_de_campo_service.py

from abc import ABC, abstractmethod
from typing import List, Optional
from salidas_de_campo.domain.entities.salida_de_campo import SalidaDeCampo


class SalidaDeCampoService(ABC):
    @abstractmethod
    def crear_salida(self, fecha_inicio, fecha_fin, descripcion, tecnicos_asignados,
                     cuerpos_de_agua_asignados) -> SalidaDeCampo:
        pass

    @abstractmethod
    def obtener_salida_por_id(self, id: int) -> Optional[SalidaDeCampo]:
        pass

    @abstractmethod
    def listar_salidas(self) -> List[SalidaDeCampo]:
        pass

    @abstractmethod
    def editar_salida(self, id: int, **datos) -> SalidaDeCampo:
        pass

    @abstractmethod
    def eliminar_salida(self, id: int) -> None:
        pass
