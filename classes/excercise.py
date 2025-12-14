class Excercise:
    def __init__(self, conn):
        self.conn = conn

    def inster(self, name, type, img):
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO Exercise (nombre, type, img) VALUES (%s, %s, %s)", (name, type, img))
            self.conn.commit()
            return True
        except:
            self.conn.rollback()


    def findAll(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM Exercise")
            rows = cur.fetchall()
            cur.close()
            return rows
        except:
            self.conn.rollback()


    def findByType(self, type):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM Exercise WHERE type = %s ORDER BY nombre;", (type,))
            rows = cur.fetchall()
            cur.close()
            return rows
        except:
            self.conn.rollback()

    def findOne(self, Id):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT * FROM Exercise WHERE Id = %s;", (Id,))
            rows = cur.fetchone()
            cur.close()
            return rows
        except:
            self.conn.rollback()
