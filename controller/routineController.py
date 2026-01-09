from modelo.routine import Routine
from controller import dayController
from typing import List
from modelo.day import Day


class routineController:
    def __init__(self, conn):
        self.conn = conn
        self.routinaConeccion = Routine(self.conn)
        self.dayConnection = Day(self.conn)


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
                _, day_id ,day_name, exercise_id,ex_name, e_img,s_id,series,reps, peso, day_exercise_id = row

                if day_name not in resultado["days"]:
                    resultado["days"][day_name] = {
                        "day_id": day_id,
                        "exercises": [],
                    }

                resultado["days"][day_name]["exercises"].append({
                    "exercise_id": exercise_id,
                    "exercise_name": ex_name,
                    "exercise_img": e_img,
                    "set_id": s_id,
                    "series": series,
                    "repeticiones": reps,
                    "peso": peso,
                    "day_exercise_id": day_exercise_id,

                })
            return resultado

        except Exception as e:
            print(e)


    def obtener_ultimos_cinco(self):
        rutinas = self.routinaConeccion.obtener_ultimos_5()

        resultado = []
        for routin in rutinas:
            id, name = routin
            days = self.dayConnection.cant_days(id)
            resultado.append({
                "id_rutina": id,
                "name": name,
                "days": days
            })

        return resultado




