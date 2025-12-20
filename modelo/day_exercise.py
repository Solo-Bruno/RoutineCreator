class DayExercise:
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



    def findByDayId(self, day_id: int, exercise_id: int):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM Day_Exercise WHERE day_id = %s AND exercise_id = %s", (day_id, exercise_id))
            ret = cursor.fetchone()[0]
            return ret
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()

    def findById(self, id: int):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM Day_Exercise WHERE id = %s", (id,))
            ret = cursor.fetchone()
            return ret
        except Exception as e:
            self.conn.rollback()
        finally:
            cursor.close()