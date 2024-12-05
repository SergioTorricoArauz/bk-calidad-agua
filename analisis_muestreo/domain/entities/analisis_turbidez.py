# analisis/domain/entities/analisis_turbidez.py
from analisis_muestreo.domain.entities import Analisis


class AnalisisTurbidez(Analisis):
    def __init__(self, turbidez: float, salida_de_campo_id: int, **kwargs):
        datos = {"turbidez": turbidez}  # Crea el diccionario de datos
        super().__init__(tipo="turbidez", salida_de_campo_id=salida_de_campo_id, datos=datos, **kwargs)
        self.turbidez = turbidez
        self.validar()

    def validar(self):
        if self.turbidez < 0:
            raise ValueError("La turbidez no puede ser negativa.")

    def clasificacion_turbidez(self) -> str:
        if self.turbidez < 1:
            return "Agua muy clara"
        elif self.turbidez <= 5:
            return "Agua ideal para consumo humano"
        elif self.turbidez <= 10:
            return "Agua ligeramente turbia"
        elif self.turbidez <= 50:
            return "Agua turbia"
        else:
            return "Agua muy turbia"

    def detalles(self) -> dict:
        return {
            "turbidez": self.turbidez,
            "clasificacion": self.clasificacion_turbidez()
        }
