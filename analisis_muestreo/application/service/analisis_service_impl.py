# analisis/application/services/analisis_service_impl.py

from typing import Dict, List, Optional
from analisis_muestreo.domain.ports.input.analisis_service import AnalisisService
from analisis_muestreo.domain.ports.output.analisis_repository import AnalisisRepository
from analisis_muestreo.application.service import AnalisisRegistry
from analisis_muestreo.domain.entities.analisis import Analisis
from analisis_muestreo.domain.exception.analisis_muestreo_exception import AnalisisMuestreoException


class AnalisisServiceImpl(AnalisisService):
    def __init__(self, analisis_repository: AnalisisRepository):
        self.analisis_repository = analisis_repository

    def registrar_analisis(self, tipo: str, salida_de_campo_id: int, datos: Dict) -> Analisis:
        """
        Registra un nuevo análisis dinámicamente basado en el tipo.
        """
        try:
            # Obtiene la clase de análisis correspondiente
            analisis_class = AnalisisRegistry.obtener(tipo)
        except ValueError as e:
            raise AnalisisMuestreoException(f"Tipo de análisis no soportado: {tipo}") from e

        try:
            # Crea una instancia de la clase de análisis pasando salida_de_campo_id y datos
            analisis = analisis_class(salida_de_campo_id=salida_de_campo_id, **datos)
        except TypeError as e:
            raise AnalisisMuestreoException(f"Error en los datos proporcionados para el tipo {tipo}: {e}") from e

        # Guarda el análisis en el repositorio
        return self.analisis_repository.guardar(analisis)
    def listar_analisis_por_salida(self, salida_de_campo_id: int) -> List[Analisis]:
        """
        Lista todos los análisis asociados a una salida de campo.
        """
        analisis_list = self.analisis_repository.obtener_todos_por_salida(salida_de_campo_id)
        if not analisis_list:
            raise AnalisisMuestreoException(
                f"No se encontraron análisis para la salida de campo con ID {salida_de_campo_id}.")
        return analisis_list

    def obtener_analisis_por_id(self, id: int) -> Optional[Analisis]:
        """
        Obtiene un análisis por su ID.
        """
        analisis = self.analisis_repository.obtener_por_id(id)
        if not analisis:
            raise AnalisisMuestreoException(f"Análisis con ID {id} no encontrado.")
        return analisis

    def clasificar_analisis(self, id: int) -> Dict:
        """
        Devuelve la clasificación específica de un análisis por su ID.
        """
        analisis = self.obtener_analisis_por_id(id)
        if isinstance(analisis, Analisis):
            if hasattr(analisis, "clasificacion_turbidez"):
                return {"tipo": "turbidez", "clasificacion": analisis.clasificacion_turbidez()}
            elif hasattr(analisis, "caudal"):
                return {"tipo": "caudal", "caudal": analisis.caudal}
            elif hasattr(analisis, "clasificacion_ph"):
                return {"tipo": "ph", "clasificacion": analisis.clasificacion_ph()}
        raise AnalisisMuestreoException(f"Tipo de análisis no reconocido para ID {id}.")

    def obtener_estadisticas(self, salida_de_campo_id: int) -> Dict:
        """
        Genera estadísticas resumidas para los análisis de una salida de campo.
        """
        analisis_list = self.listar_analisis_por_salida(salida_de_campo_id)

        if not analisis_list:
            raise AnalisisMuestreoException(
                f"No se encontraron análisis para la salida de campo con ID {salida_de_campo_id}.")

        estadisticas = {
            "total_analisis": len(analisis_list),
            "promedio_turbidez": None,
            "promedio_caudal": None,
            "promedio_ph": None
        }

        turbidez_vals = [a.turbidez for a in analisis_list if hasattr(a, "turbidez")]
        caudal_vals = [a.caudal for a in analisis_list if hasattr(a, "caudal")]
        ph_vals = [a.ph for a in analisis_list if hasattr(a, "ph")]

        if turbidez_vals:
            estadisticas["promedio_turbidez"] = sum(turbidez_vals) / len(turbidez_vals)
        if caudal_vals:
            estadisticas["promedio_caudal"] = sum(caudal_vals) / len(caudal_vals)
        if ph_vals:
            estadisticas["promedio_ph"] = sum(ph_vals) / len(ph_vals)

        return estadisticas

    def eliminar_analisis(self, id: int) -> None:
        """
        Elimina un análisis si cumple las condiciones.
        """
        analisis = self.obtener_analisis_por_id(id)
        if not analisis:
            raise AnalisisMuestreoException(f"Análisis con ID {id} no encontrado.")

        # Aquí se podrían agregar reglas de negocio para validar si puede eliminarse
        try:
            self.analisis_repository.eliminar(id)
        except Exception as e:
            raise AnalisisMuestreoException(f"Error al eliminar el análisis con ID {id}: {e}")
