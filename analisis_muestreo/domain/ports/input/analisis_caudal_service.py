from abc import ABC, abstractmethod
from typing import List, Optional
from analisis_muestreo.domain.entities.analisis_caudal import AnalisisCaudal


class AnalisisCaudalService(ABC):
    @abstractmethod
    def crear_analisis(self, velocidad: float, ancho: float, profundidad_media: float, fecha,
                       tecnico_id: int, salida_id: int) -> AnalisisCaudal:
        pass

    @abstractmethod
    def obtener_analisis_por_id(self, id: int) -> Optional[AnalisisCaudal]:
        pass

    @abstractmethod
    def listar_analisis_por_salida(self, salida_id: int) -> List[AnalisisCaudal]:
        pass

    @abstractmethod
    def eliminar_analisis(self, id: int) -> None:
        pass

    @abstractmethod
    def actualizar_analisis(self, id: int, velocidad: float, ancho: float,
                             profundidad_media: float, fecha, tecnico_id: int, salida_id: int) -> AnalisisCaudal:
        pass
