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

    def obtener_datos_rutina_completa(self, routine_id):
        try:
            rows = self.routinaConeccion.obtener_datos_rutina_completa(routine_id)
            resultado = {
                "id_rutina": routine_id,
                "name": rows[0][0],
                "days": {}
            }

            for row in rows:
                _, day_name, ex_name, series, reps, peso = row

                if day_name not in resultado["days"]:
                    resultado["days"][day_name] = []

                resultado["days"][day_name].append({
                    "exercise_name": ex_name,
                    "series": series,
                    "repeticiones": reps,
                    "peso": peso
                })

            return resultado

        except Exception as e:
            print(e)
