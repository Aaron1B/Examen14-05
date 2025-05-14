from src.proceso import Proceso
from src.fcfs_scheduler import FCFSScheduler
from src.repositorio_procesos import RepositorioProcesos

def main():
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso(pid="P1", duracion=5, prioridad=1))
    repo.agregar_proceso(Proceso(pid="P2", duracion=3, prioridad=2))
    repo.agregar_proceso(Proceso(pid="P3", duracion=8, prioridad=1))

    print("Procesos registrados:")
    for proceso in repo.listar_procesos():
        print(vars(proceso))

    scheduler = FCFSScheduler()
    procesos = repo.listar_procesos()
    gantt_chart = scheduler.planificar(procesos)
    print("\nDiagrama de Gantt:")
    for entry in gantt_chart:
        print(entry)

    metricas = scheduler.calcular_metricas(procesos, gantt_chart)
    print("\nMétricas:")
    for m in metricas["metricas"]:
        print(m)
    print("\nPromedios:")
    print(metricas["promedios"])

if __name__ == "__main__":
    main()
