from modelo.set import Set

class setController:
    def __init__(self, conn):
        self.conn = conn
        self.set = Set(self.conn)


    def insert(self, day_id:int, cant:int, reps:int, peso:int):
        try:
            set_id = self.set.create(cant, reps, day_id, peso)
            obj = self.set.findById(set_id)
            return obj
        except Exception as e:
            raise e

    def findById(self, set_id:int):
        try:
            set_id = self.set.findById(set_id)
            return set_id
        except Exception as e:
            raise e


    def deleteById(self, set_id:int):
        try:
            self.set.delete(set_id)
        except Exception as e:
            raise e
