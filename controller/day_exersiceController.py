from modelo.day_exercise import DayExercise
from controller.setController import setController

class DayExersiceController:
    def __init__(self, conn):
        self.conn = conn
        self.day_exercise = DayExercise(self.conn)
        self.set = setController(self.conn)



    def insert(self, day_id:int, exercise_id:int, repeticiones:int, series:int, peso:int):
        try:
            cant = self.day_exercise.findCantByDayId(day_id, exercise_id)
            day_exercise_id = self.day_exercise.insert(day_id, exercise_id, cant+1)
            set = self.set.insert(day_exercise_id, series, repeticiones, peso)
            objSet = {
                'day_exercise_id': day_exercise_id,
                'set_id': set[0],
                'series': set[1],
                'repeticiones': set[2],
                'peso': set[3]
            }
            return objSet

        except Exception as e:
            raise e

    def delete(self, day_exercise_id:int, set_id:int):
        try:
            self.set.deleteById(set_id)
            self.day_exercise.delete(day_exercise_id)
            print('delete')
        except Exception as e:
            raise e
