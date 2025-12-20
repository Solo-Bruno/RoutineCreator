from typing import List
from modelo import day

class DayController:
    def __init__(self, conn):
        self.conn = conn
        self.day = day.Day(self.conn)

    def createDays(self, days: List[str], routineId: int):
        try:
            for day in days:
                self.day.insert(day, routineId)
        except Exception as e:
            raise e

    def findDayByRoutineId(self, routineId: int):
        try:
            ret = self.day.findAllByRoutineId(routineId)
            return ret
        except Exception as e:
            raise e
