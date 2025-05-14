from src.proceso import Proceso
from src.fcfs_scheduler import FCFSScheduler
from src.repositorio_procesos import RepositorioProcesos

def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Agregar proceso")
    print("2. Listar procesos")
    print("3. Seleccionar algoritmo de planificación")
    print("4. Ejecutar simulación y mostrar resultados")
    print("5. Guardar procesos")
    print("6. Cargar procesos")
    print("7. Salir")

def main():
    repo = RepositorioProcesos()
    scheduler = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pid = input("Ingrese el PID del proceso: ")
            duracion = int(input("Ingrese la duración del proceso: "))
            prioridad = int(input("Ingrese la prioridad del proceso: "))
            try:
                proceso = Proceso(pid=pid, duracion=duracion, prioridad=prioridad)
                if repo.agregar_proceso(proceso):
                    print("Proceso agregado correctamente.")
                else:
                    print("Error: Ya existe un proceso con ese PID.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            print("\nProcesos registrados:")
            for proceso in repo.listar_procesos():
                print(vars(proceso))

        elif opcion == "3":
            print("\nSeleccione el algoritmo de planificación:")
            print("1. FCFS (First-Come, First-Served)")
            algoritmo = input("Seleccione una opción: ")
            if algoritmo == "1":
                scheduler = FCFSScheduler()
                print("Algoritmo FCFS seleccionado.")
            else:
                print("Opción inválida.")

        elif opcion == "4":
            if not scheduler:
                print("Error: Seleccione un algoritmo de planificación primero.")
                continue
            procesos = repo.listar_procesos()
            if not procesos:
                print("Error: No hay procesos registrados.")
                continue
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

        elif opcion == "5":
            formato = input("Seleccione el formato (json/csv): ").lower()
            filepath = input("Ingrese el nombre del archivo: ")
            if formato == "json":
                repo.guardar_json(filepath)
                print("Procesos guardados en formato JSON.")
            elif formato == "csv":
                repo.guardar_csv(filepath)
                print("Procesos guardados en formato CSV.")
            else:
                print("Formato inválido.")

        elif opcion == "6":
            formato = input("Seleccione el formato (json/csv): ").lower()
            filepath = input("Ingrese el nombre del archivo: ")
            if formato == "json":
                repo.cargar_json(filepath)
                print("Procesos cargados desde archivo JSON.")
            elif formato == "csv":
                repo.cargar_csv(filepath)
                print("Procesos cargados desde archivo CSV.")
            else:
                print("Formato inválido.")

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
