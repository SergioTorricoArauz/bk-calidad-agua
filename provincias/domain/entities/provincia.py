# provincias/domain/entities/provincia.py

from typing import Optional

from provincias.domain.exception import ProvinciaException


class Provincia:
    def __init__(self, nombre: str, departamento_id: int, id: Optional[int] = None):
        if not nombre:
            raise ProvinciaException("El nombre de la provincia no puede estar vacío.")
        if not departamento_id:
            raise ProvinciaException("El departamento_id de la provincia no puede estar vacío.")

        self.id = id
        self.nombre = nombre
        self.departamento_id = departamento_id

    def __str__(self):
        return f"Provincia(id={self.id}, nombre={self.nombre}, departamento_id={self.departamento_id})"
