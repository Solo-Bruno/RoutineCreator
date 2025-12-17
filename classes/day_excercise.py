class DayExcercise:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, day_id: int, exercise_id: int, orden: int):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO Day_Exercise (day_id, exercise_id, orden) VALUES (%s,%s,%s) RETURNING id;", (day_id, exercise_id, orden))
            self.conn.commit()
            ret = cursor.fetchone()[0]
            return ret
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()


