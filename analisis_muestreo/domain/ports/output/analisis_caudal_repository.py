# analisis_muestreo/domain/ports/output/analisis_caudal_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from analisis_muestreo.domain.entities.analisis_caudal import AnalisisCaudal


class AnalisisCaudalRepository(ABC):
    @abstractmethod
    def guardar(self, analisis: AnalisisCaudal) -> AnalisisCaudal:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[AnalisisCaudal]:
        pass

    @abstractmethod
    def listar_por_salida(self, salida_id: int) -> List[AnalisisCaudal]:
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        pass

    @abstractmethod
    def actualizar(self, analisis: AnalisisCaudal) -> AnalisisCaudal:
        pass
