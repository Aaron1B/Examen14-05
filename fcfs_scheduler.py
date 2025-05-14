from typing import List
from scheduler import Scheduler, GanttEntry
from proceso import Proceso

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        tiempo_actual = 0
        gantt_chart = []

        for proceso in procesos:
            inicio = tiempo_actual
            fin = inicio + proceso.duracion
            gantt_chart.append((proceso.nombre, inicio, fin))
            tiempo_actual = fin

        return gantt_chart
