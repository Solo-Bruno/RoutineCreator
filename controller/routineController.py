from modelo.routine import Routine
from controller import dayController
from typing import List


class routineController:
    def __init__(self, conn):
        self.conn = conn
        self.routinaConeccion = Routine(self.conn)


    def crearRutina(self, name: str, dias: List[str]):
        try:
            newRoutineId = self.routinaConeccion.insert(name)
            dayController.DayController(self.conn).createDays(dias, newRoutineId)
            return newRoutineId
        except Exception as e:
            print(e)

    def obtener_datos_rutina_completa(self, routine_id: int):
        try:
            self.routinaConeccion.obtener_datos_rutina_completa(routine_id)
        except Exception as e:
            print(e)
