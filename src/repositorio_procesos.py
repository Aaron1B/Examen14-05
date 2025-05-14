import json
import csv
from typing import List, Optional
from proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        self.procesos = {}

    def agregar_proceso(self, proceso: Proceso) -> bool:
        if proceso.pid in self.procesos:
            return False
        self.procesos[proceso.pid] = proceso
        return True

    def listar_procesos(self) -> List[Proceso]:
        return list(self.procesos.values())

    def eliminar_proceso(self, pid: int) -> bool:
        if pid in self.procesos:
            del self.procesos[pid]
            return True
        return False

    def obtener_proceso(self, pid: int) -> Optional[Proceso]:
        return self.procesos.get(pid)

    def guardar_json(self, filepath: str) -> None:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump([proceso.__dict__ for proceso in self.procesos.values()], file, ensure_ascii=False, indent=4)

    def cargar_json(self, filepath: str) -> None:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.procesos = {item['pid']: Proceso(**item) for item in data}

    def guardar_csv(self, filepath: str) -> None:
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad', 'tiempo_restante', 'tiempo_llegada', 'tiempo_inicio', 'tiempo_fin'])
            for proceso in self.procesos.values():
                writer.writerow([proceso.pid, proceso.duracion, proceso.prioridad, proceso.tiempo_restante, 
                                 proceso.tiempo_llegada, proceso.tiempo_inicio, proceso.tiempo_fin])

    def cargar_csv(self, filepath: str) -> None:
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            self.procesos = {}
            for row in reader:
                row['duracion'] = int(row['duracion'])
                row['prioridad'] = int(row['prioridad'])
                row['tiempo_restante'] = int(row['tiempo_restante'])
                row['tiempo_llegada'] = int(row['tiempo_llegada'])
                row['tiempo_inicio'] = None if row['tiempo_inicio'] == 'None' else int(row['tiempo_inicio'])
                row['tiempo_fin'] = None if row['tiempo_fin'] == 'None' else int(row['tiempo_fin'])
                self.procesos[row['pid']] = Proceso(**row)
