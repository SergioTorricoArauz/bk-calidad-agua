# analisis/domain/ports/output/analisis_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional, Dict

from analisis_muestreo.domain.entities import Analisis


class AnalisisRepository(ABC):
    @abstractmethod
    def guardar(self, analisis: Analisis) -> Analisis:
        """Persiste un nuevo análisis en la base de datos."""
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Analisis]:
        """Recupera un análisis específico por su ID."""
        pass

    @abstractmethod
    def obtener_todos_por_salida(self, salida_de_campo_id: int) -> List[Analisis]:
        """Recupera todos los análisis asociados a una salida de campo."""
        pass

    @abstractmethod
    def obtener_clasificacion(self, id: int) -> Dict:
        """Recupera la clasificación específica de un análisis."""
        pass

    @abstractmethod
    def obtener_estadisticas(self, salida_de_campo_id: int) -> Dict:
        """Calcula estadísticas resumidas para los análisis de una salida."""
        pass

    @abstractmethod
    def eliminar(self, id: int) -> None:
        """Elimina un análisis específico por su ID."""
        pass
