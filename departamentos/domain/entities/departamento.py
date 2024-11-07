# departametos/domain/entities/departamento.py

from departamentos.domain.exception import DepartamentoError

from typing import Optional


class Departamento:
    def __init__(self, nombre: str, id: Optional[int] = None):
        if not nombre:
            raise DepartamentoError("El nombre del departamento no puede estar vacío.")

        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Departamento(id={self.id}, nombre={self.nombre})"
