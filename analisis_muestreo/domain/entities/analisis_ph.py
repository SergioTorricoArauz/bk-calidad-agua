# analisis/domain/entities/analisis_ph.py

from analisis_muestreo.domain.entities import Analisis


class AnalisisPH(Analisis):
    def __init__(self, ph: float, salida_de_campo_id: int, **kwargs):
        """
        Constructor para el análisis de pH.
        :param ph: Valor del pH.
        :param salida_de_campo_id: ID de la salida de campo relacionada.
        :param kwargs: Argumentos adicionales para la clase base.
        """
        # Crear el diccionario de datos para la clase base
        datos = {"ph": ph, "clasificacion": self._clasificar_ph(ph)}

        super().__init__(tipo="ph", salida_de_campo_id=salida_de_campo_id, datos=datos, **kwargs)

        # Asignar valores específicos
        self.ph = ph
        self.salida_de_campo_id = salida_de_campo_id

        # Validar el valor de pH
        self.validar()

    @staticmethod
    def _clasificar_ph(ph: float) -> str:
        """
        Clasifica el pH en categorías (Ácido, Neutral, Alcalino).
        :param ph: Valor del pH.
        :return: La clasificación del pH como cadena.
        """
        if ph < 7:
            return "Ácido"
        elif ph == 7:
            return "Neutral"
        else:
            return "Alcalino"

    def validar(self):
        """
        Valida el valor del pH.
        """
        if not (0 <= self.ph <= 14):
            raise ValueError("El valor del pH debe estar entre 0 y 14.")

    def detalles(self) -> dict:
        """
        Devuelve los detalles específicos del análisis de pH.
        :return: Un diccionario con los detalles del análisis.
        """
        return {
            "ph": self.ph,
            "clasificacion": self._clasificar_ph(self.ph)
        }
