from typing import List
from src.scheduler import Scheduler, GanttEntry
from proceso import Proceso

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        tiempo_actual = 0
        gantt_chart = []
        cola = procesos[:]

        while cola:
            proceso = cola.pop(0)
            if proceso.duracion > self.quantum:
                inicio = tiempo_actual
                fin = inicio + self.quantum
                gantt_chart.append((proceso.nombre, inicio, fin))
                tiempo_actual = fin
                proceso.duracion -= self.quantum
                cola.append(proceso)
            else:
                inicio = tiempo_actual
                fin = inicio + proceso.duracion
                gantt_chart.append((proceso.nombre, inicio, fin))
                tiempo_actual = fin

        return gantt_chart
