from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso

GanttEntry = Tuple[str, int, int]

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        pass

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        gantt_chart = []
        queue = procesos[:]
        time = 0

        while queue:
            proceso = queue.pop(0)
            execution_time = min(proceso.tiempo_restante, self.quantum)
            gantt_chart.append((proceso.nombre, time, time + execution_time))
            time += execution_time
            proceso.tiempo_restante -= execution_time

            if proceso.tiempo_restante > 0:
                queue.append(proceso)

        return gantt_chart
