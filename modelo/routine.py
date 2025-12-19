
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