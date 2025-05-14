class Proceso:
    _pids_existentes = set() 

    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("El pid no puede estar vacío.")
        if pid in Proceso._pids_existentes:
            raise ValueError(f"El pid '{pid}' ya existe.")
        if duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        if prioridad < 0:
            raise ValueError("La prioridad debe ser un entero no negativo.")
        
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None

        Proceso._pids_existentes.add(pid)

    def __repr__(self):
        return f"Proceso(pid='{self.pid}', duracion={self.duracion}, prioridad={self.prioridad}, tiempo_restante={self.tiempo_restante}, tiempo_llegada={self.tiempo_llegada}, tiempo_inicio={self.tiempo_inicio}, tiempo_fin={self.tiempo_fin})"
