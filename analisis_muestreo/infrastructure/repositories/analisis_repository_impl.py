# analisis/infrastructure/repositories/analisis_repository_impl.py

from typing import List, Optional, Dict
from analisis_muestreo.domain.entities.analisis_turbidez import AnalisisTurbidez
from analisis_muestreo.domain.entities.analisis_caudal import AnalisisCaudal
from analisis_muestreo.domain.entities.analisis_ph import AnalisisPH
from analisis_muestreo.domain.entities.analisis import Analisis
from analisis_muestreo.domain.ports.output.analisis_repository import AnalisisRepository
from analisis_muestreo.infrastructure.models.analisis_model import AnalisisModel


class AnalisisRepositoryImpl(AnalisisRepository):
    def obtener_clasificacion(self, id: int) -> Dict:
        """
        Recupera la clasificación específica de un análisis basado en su ID.
        """
        analisis = self.obtener_por_id(id)
        if not analisis:
            raise ValueError(f"No se encontró el análisis con ID {id}")

        if isinstance(analisis, AnalisisTurbidez):
            return {"tipo": "turbidez", "clasificacion": analisis.clasificacion_turbidez()}
        elif isinstance(analisis, AnalisisCaudal):
            return {"tipo": "caudal", "caudal": analisis.caudal}
        elif isinstance(analisis, AnalisisPH):
            return {"tipo": "ph", "clasificacion": analisis.clasificacion_ph()}
        else:
            raise ValueError(f"Tipo de análisis no reconocido para ID {id}")

    def obtener_estadisticas(self, salida_de_campo_id: int) -> Dict:
        """
        Genera estadísticas resumidas de los análisis asociados a una salida de campo.
        """
        analisis_list = self.obtener_todos_por_salida(salida_de_campo_id)

        estadisticas = {
            "total_analisis": len(analisis_list),
            "promedio_turbidez": None,
            "promedio_caudal": None,
            "promedio_ph": None,
        }

        # Cálculos de promedios
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

    def eliminar(self, id: int) -> None:
        """
        Elimina un análisis de la base de datos basado en su ID.
        """
        try:
            analisis_model = AnalisisModel.objects.get(id=id)
            analisis_model.delete()
        except AnalisisModel.DoesNotExist:
            raise ValueError(f"No se encontró el análisis con ID {id}")

    def guardar(self, analisis: Analisis) -> Analisis:
        """
        Persiste un nuevo análisis en la base de datos.
        """
        datos = analisis.datos  # Usamos el método datos
        analisis_model = AnalisisModel.objects.create(
            tipo=analisis.tipo,
            salida_de_campo_id=analisis.salida_de_campo_id,
            datos=datos,  # Guardamos los datos como JSON
        )
        analisis.id = analisis_model.id
        return analisis

    def obtener_por_id(self, id: int) -> Optional[Analisis]:
        """
        Recupera un análisis específico por su ID.
        """
        try:
            # Obtiene el modelo desde la base de datos
            analisis_model = AnalisisModel.objects.get(id=id)
            # Convierte el modelo a una entidad del dominio
            return self._convertir_a_entidad(analisis_model)  # Llamada correcta como método de instancia
        except AnalisisModel.DoesNotExist:
            return None

    def obtener_todos_por_salidas(self, salidas_ids: Optional[List[int]] = None) -> List[Analisis]:
        """
        Recupera todos los análisis asociados a una lista de IDs de salidas de campo.
        Si salidas_ids es None, recupera todos los análisis.
        :param salidas_ids: Lista de IDs de salidas de campo.
        """
        if salidas_ids is None:
            analisis_models = AnalisisModel.objects.all()
        else:
            analisis_models = AnalisisModel.objects.filter(salida_de_campo_id__in=salidas_ids)

        return [self._convertir_a_entidad(am) for am in analisis_models]

    def obtener_todos_por_salida(self, salida_de_campo_id: int) -> List[Analisis]:
        """
        Recupera todos los análisis asociados a una salida de campo específica.
        """
        analisis_models = AnalisisModel.objects.filter(salida_de_campo_id=salida_de_campo_id)
        return [self._convertir_a_entidad(am) for am in analisis_models]

    @staticmethod
    def _convertir_a_datos(analisis: Analisis) -> Dict:
        """Convierte la entidad a datos JSON para almacenarlo en la base de datos."""
        return analisis.datos  # Usamos el método datos para obtener los datos específicos

    @staticmethod
    def _convertir_a_entidad(analisis_model: AnalisisModel) -> Analisis:
        """
        Convierte un modelo de base de datos en una entidad del dominio.
        """
        datos = analisis_model.datos
        salida_de_campo_id = analisis_model.salida_de_campo_id  # Obtiene el ID de la salida de campo relacionada

        if analisis_model.tipo == "turbidez":
            return AnalisisTurbidez(
                id=analisis_model.id,
                turbidez=datos["turbidez"],
                salida_de_campo_id=salida_de_campo_id,
                fecha=analisis_model.fecha
            )
        elif analisis_model.tipo == "caudal":
            return AnalisisCaudal(
                id=analisis_model.id,
                velocidad=datos["velocidad"],
                ancho=datos["ancho"],
                profundidad_media=datos["profundidad_media"],
                salida_de_campo_id=salida_de_campo_id,
                fecha=analisis_model.fecha
            )
        elif analisis_model.tipo == "ph":
            return AnalisisPH(
                id=analisis_model.id,
                ph=datos["ph"],
                salida_de_campo_id=salida_de_campo_id,
                fecha=analisis_model.fecha
            )
        else:
            raise ValueError(f"Tipo de análisis no reconocido: {analisis_model.tipo}")
