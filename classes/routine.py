
class Routine:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, name):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO Routine (name) VALUES (%s);", (name,))
            self.conn.commit()
            return cursor.fetchone()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()

    def findById(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * from Routine WHERE id = %s;", (id,))
            return cursor.fetchone()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()
