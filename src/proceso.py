class Proceso:
    _pids = set()

    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid or pid in Proceso._pids:
            raise ValueError("PID must be unique and non-empty.")
        if duracion <= 0:
            raise ValueError("Duración must be a positive integer.")
        if not isinstance(prioridad, int):
            raise ValueError("Prioridad must be an integer.")

        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None

        Proceso._pids.add(pid)

    def __del__(self):
        Proceso._pids.discard(self.pid)
