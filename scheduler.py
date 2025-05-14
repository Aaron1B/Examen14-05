from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso

GanttEntry = Tuple[str, int, int]  # Alias for GanttEntry type

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """
        Planifica los procesos y devuelve una lista de entradas de Gantt.
        Cada entrada es una tupla (pid, tiempo_inicio, tiempo_fin).
        """
        pass
