# cuerpos_de_agua/domain/entities/cuerpo_de_agua.py

from typing import Optional
from cuerpos_de_agua.domain.exception.cuerpo_de_agua_exception import CuerpoDeAguaException


class CuerpoDeAgua:
    TIPO_RIO = 1
    TIPO_ARROYO = 2
    TIPO_LAGO = 3
    TIPO_HUMEDAL = 4

    TIPOS_VALIDOS = [TIPO_RIO, TIPO_ARROYO, TIPO_LAGO, TIPO_HUMEDAL]

    def __init__(self, nombre: str, tipo: str, comunidad_id: int, latitud: Optional[float] = None,
                 longitud: Optional[float] = None, id: Optional[int] = None):
        if tipo not in self.TIPOS_VALIDOS:
            raise CuerpoDeAguaException("Tipo de cuerpo de agua inválido.")
        if not nombre:
            raise CuerpoDeAguaException("Nombre es un campo obligatorio.")
        if not comunidad_id:
            raise CuerpoDeAguaException("Comunidad ID es un campo obligatorio.")

        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.latitud = latitud
        self.longitud = longitud
        self.comunidad_id = comunidad_id

    def __str__(self):
        return f"CuerpoDeAgua(id={self.id}, nombre={self.nombre}, tipo={self.tipo}, comunidad_id={self.comunidad_id})"
