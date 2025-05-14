from typing import List
from scheduler import Scheduler, GanttEntry
from proceso import Proceso

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """
        Planifica los procesos según el orden de llegada (First-Come, First-Served).
        """
        tiempo_actual = 0
        gantt_chart = []

        for proceso in procesos:
            tiempo_inicio = tiempo_actual
            tiempo_fin = tiempo_inicio + proceso.duracion
            gantt_chart.append((proceso.pid, tiempo_inicio, tiempo_fin))
            tiempo_actual = tiempo_fin

        return gantt_chart
