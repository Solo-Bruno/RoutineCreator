class Set:
    def __init__(self, conn):
        self.conn = conn


    def create(self, cant: int, rep: int, day_exercise_id: int, peso: int):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO Set(cantidad,repeticiones,day_exercise_id, peso) VALUES (%s, %s, %s, %s) RETURNING id;", (cant,rep,day_exercise_id,peso))
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
            cursor.execute("SELECT * FROM Set WHERE id = %s;", (id,))
            ret = cursor.fetchone()
            return ret
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()



    def delete(self, id: int):
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM Set WHERE id = %s;", (id,))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()