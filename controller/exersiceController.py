from modelo.exercise import Exercise

class ExcerciseController:
    def __init__(self, conn):
        self.conn = conn
        self.exercise = Exercise(self.conn)


    def findAllExcercises(self):
        try:
            ret = self.exercise.findAll()
            return ret
        except Exception as e:
            raise e

    def findByTypeExcercise(self, exerciseType):
        try:
            ret = self.exercise.findByType(exerciseType)
            return ret
        except Exception as e:
            raise e
