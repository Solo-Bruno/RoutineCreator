from modelo.excercise import Excercise

class ExcerciseController:
    def __init__(self, conn):
        self.conn = conn
        self.excercise = Excercise(self.conn)


    def findAllExcercises(self):
        try:
            ret = self.excercise.findAll()
            return ret
        except Exception as e:
            raise e

    def findByTypeExcercise(self, excerciseType):
        try:
            ret = self.excercise.findByType(excerciseType)
            return ret
        except Exception as e:
            raise e
