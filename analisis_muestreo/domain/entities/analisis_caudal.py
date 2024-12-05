# analisis/domain/entities/analisis_caudal.py

from analisis_muestreo.domain.entities import Analisis


class AnalisisCaudal(Analisis):
    def __init__(self, velocidad: float, ancho: float, profundidad_media: float, salida_de_campo_id: int, **kwargs):
        """
        Constructor para análisis de caudal.
        :param velocidad: Velocidad del flujo (m/s).
        :param ancho: Ancho del cuerpo de agua (m).
        :param profundidad_media: Profundidad media del cuerpo de agua (m).
        :param salida_de_campo_id: ID de la salida de campo relacionada.
        :param kwargs: Argumentos adicionales para la clase base.
        """
        # Crear el diccionario de datos para la clase base
        datos = {
            "velocidad": velocidad,
            "ancho": ancho,
            "profundidad_media": profundidad_media,
            "caudal": self._calcular_caudal(velocidad, ancho, profundidad_media),
        }

        super().__init__(tipo="caudal", salida_de_campo_id=salida_de_campo_id, datos=datos, **kwargs)

        # Asignar valores específicos
        self.velocidad = velocidad
        self.ancho = ancho
        self.profundidad_media = profundidad_media
        self.caudal = datos["caudal"]

        # Validar los datos
        self.validar()

    @staticmethod
    def _calcular_caudal(velocidad: float, ancho: float, profundidad_media: float) -> float:
        """
        Calcula el caudal en metros cúbicos por segundo (m³/s).
        :param velocidad: Velocidad del flujo (m/s).
        :param ancho: Ancho del cuerpo de agua (m).
        :param profundidad_media: Profundidad media (m).
        :return: El caudal calculado.
        """
        return velocidad * ancho * profundidad_media

    def validar(self):
        """
        Valida los atributos del análisis de caudal.
        """
        if self.velocidad < 0:
            raise ValueError("La velocidad debe ser positiva.")
        if self.ancho <= 0:
            raise ValueError("El ancho debe ser mayor que 0.")
        if self.profundidad_media <= 0:
            raise ValueError("La profundidad media debe ser mayor que 0.")

    def detalles(self) -> dict:
        """
        Devuelve los detalles específicos del análisis de caudal.
        :return: Un diccionario con los detalles del análisis.
        """
        return {
            "velocidad": self.velocidad,
            "ancho": self.ancho,
            "profundidad_media": self.profundidad_media,
            "caudal": self.caudal,
        }
