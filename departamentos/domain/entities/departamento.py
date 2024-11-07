from departamentos.domain.exception import DepartamentoError


class Departamento:
    def __init__(self, nombre: str):
        self.nombre = nombre
        if not nombre:
            raise DepartamentoError("El nombre del departamento no puede estar vacio")

    def __str__(self):
        return f"Departamento: {self.nombre}"
