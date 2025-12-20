from typing import List

class Day:
    def __init__(self, conn):
        self.conn = conn


    def insert(self, day:str, routine_id: int):
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO Day (name, routine_id) VALUES (%s, %s);", (day, routine_id))
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cur.close()

    def findAllByRoutineId(self, routine_id: int):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT id, name FROM Day WHERE routine_id = %s;", (routine_id,))
            rows = cur.fetchall()
            return rows
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cur.close()

    def findById(self, day_id: int, routine_id: int):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM Day WHERE id = %s;", (day_id,))
            day = cur.fetchOne()
            return day
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cur.close()

