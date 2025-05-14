from typing import List
from src.scheduler import Scheduler, GanttEntry
from proceso import Proceso

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        tiempo_actual = 0
        gantt_chart = []

        for proceso in procesos:
            inicio = tiempo_actual
            fin = inicio + proceso.duracion
            gantt_chart.append((proceso.pid, inicio, fin))  
            tiempo_actual = fin

        return gantt_chart

    def calcular_metricas(self, procesos: List[Proceso], gantt_chart: List[GanttEntry]) -> dict:
        metricas = []
        for proceso in procesos:
            for pid, inicio, fin in gantt_chart:
                if pid == proceso.pid:
                    proceso.tiempo_inicio = proceso.tiempo_inicio or inicio
                    proceso.tiempo_fin = fin

            tiempo_respuesta = proceso.tiempo_inicio - proceso.tiempo_llegada
            tiempo_retorno = proceso.tiempo_fin - proceso.tiempo_llegada
            tiempo_espera = tiempo_retorno - proceso.duracion

            metricas.append({
                "pid": proceso.pid,
                "tiempo_respuesta": tiempo_respuesta,
                "tiempo_retorno": tiempo_retorno,
                "tiempo_espera": tiempo_espera
            })

        promedios = {
            "promedio_tiempo_respuesta": sum(m["tiempo_respuesta"] for m in metricas) / len(metricas),
            "promedio_tiempo_retorno": sum(m["tiempo_retorno"] for m in metricas) / len(metricas),
            "promedio_tiempo_espera": sum(m["tiempo_espera"] for m in metricas) / len(metricas)
        }

        return {"metricas": metricas, "promedios": promedios}
