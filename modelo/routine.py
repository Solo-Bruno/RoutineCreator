
class Routine:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, name):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO Routine (name) VALUES (%s) RETURNING id;;", (name,))
            self.conn.commit()
            ret =  cursor.fetchone()[0]
            return ret
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()

    def findById(self, id: int):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * from Routine WHERE id = %s;", (id,))
            ret = cursor.fetchone()
            return ret
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()

    def findAll(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * from Routine;")
            return cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
        finally:
            cursor.close()

    def obtener_datos_rutina_completa(self, routine_id: int):
        cursor = self.conn.cursor()
        try:
            query = """
                SELECT 
                    r.name as routine_name,
                    d.id as day_id,
                    d.name as day_name,
                    e.id as exercise_id,
                    e.nombre as exercise_name,
                    e.img as exercise_img,
                    s.id as set_id,
                    s.cantidad as series,
                    s.repeticiones as reps,
                    s.peso as peso,
                    de.id as day_exercise_id
                FROM Routine r
                JOIN Day d ON r.id = d.routine_id
                JOIN Day_Exercise de ON d.id = de.day_id
                JOIN Exercise e ON de.exercise_id = e.id
                JOIN Set s ON de.id = s.day_exercise_id
                WHERE r.id = %s
                ORDER BY d.id, de.id;
                """
            cursor.execute(query, (routine_id,))
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()

    def obtener_ultimos_5(self):
        cursor = self.conn.cursor()
        try:
            query = "SELECT * FROM Routine as r ORDER BY r.id DESC LIMIT 5;"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()

