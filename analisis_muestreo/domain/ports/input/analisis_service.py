# analisis/domain/ports/input/analisis_service.py

from abc import ABC, abstractmethod
from typing import List, Optional, Dict

from analisis_muestreo.domain.entities import Analisis


class AnalisisService(ABC):
    @abstractmethod
    def registrar_analisis(self, tipo: str, salida_de_campo_id: int, datos: Dict) -> Analisis:
        """Registra un nuevo análisis de un tipo específico para una salida de campo."""
        pass

    @abstractmethod
    def listar_analisis_por_salida(self, salida_de_campo_id: int) -> List[Analisis]:
        """Lista todos los análisis asociados a una salida de campo."""
        pass

    @abstractmethod
    def obtener_analisis_por_id(self, id: int) -> Optional[Analisis]:
        """Obtiene un análisis por su ID."""
        pass

    @abstractmethod
    def clasificar_analisis(self, id: int) -> Dict:
        """Devuelve la clasificación específica de un análisis por su ID."""
        pass

    @abstractmethod
    def obtener_estadisticas(self, salida_de_campo_id: int) -> Dict:
        """Genera estadísticas resumidas para los análisis de una salida."""
        pass

    @abstractmethod
    def eliminar_analisis(self, id: int) -> None:
        """Elimina un análisis si cumple condiciones específicas."""
        pass
