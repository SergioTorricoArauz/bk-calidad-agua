# comunidades/domain/entities/comunidades.py

from typing import Optional
from comunidades.domain.exception.comunidad_exception import ComunidadException


class Comunidad:
    def __init__(self, nombre: str, provincia_id: int, id: Optional[int] = None):
        if not nombre:
            raise ComunidadException("El nombre de la comunidades no puede estar vacío.")
        if not provincia_id:
            raise ComunidadException("La provincia de la comunidades no puede estar vacía.")

        self.id = id
        self.nombre = nombre
        self.provincia_id = provincia_id

    def __str__(self):
        return f"Comunidad(id={self.id}, nombre={self.nombre}, provincia_id={self.provincia_id})"
