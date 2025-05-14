import pytest
from src.proceso import Proceso
from src.fcfs_scheduler import FCFSScheduler
from src.repositorio_procesos import RepositorioProcesos

@pytest.fixture
def procesos():
    return [
        Proceso(pid="P1", duracion=5, prioridad=1),
        Proceso(pid="P2", duracion=3, prioridad=2),
        Proceso(pid="P3", duracion=8, prioridad=1)
    ]

def test_fcfs_scheduler(procesos):
    scheduler = FCFSScheduler()
    gantt_chart = scheduler.planificar(procesos)

    assert gantt_chart == [
        ("P1", 0, 5),
        ("P2", 5, 8),
        ("P3", 8, 16)
    ]

    metricas = scheduler.calcular_metricas(procesos, gantt_chart)
    assert metricas["promedios"]["promedio_tiempo_respuesta"] == 4.0
    assert metricas["promedios"]["promedio_tiempo_retorno"] == 10.0
    assert metricas["promedios"]["promedio_tiempo_espera"] == 5.0

def test_repositorio_procesos(procesos, tmp_path):
    repo = RepositorioProcesos()
    for proceso in procesos:
        assert repo.agregar_proceso(proceso)

    assert len(repo.listar_procesos()) == 3

    # Test JSON persistence
    json_file = tmp_path / "procesos.json"
    repo.guardar_json(json_file)
    repo.cargar_json(json_file)
    assert len(repo.listar_procesos()) == 3

    # Test CSV persistence
    csv_file = tmp_path / "procesos.csv"
    repo.guardar_csv(csv_file)
    repo.cargar_csv(csv_file)
    assert len(repo.listar_procesos()) == 3
