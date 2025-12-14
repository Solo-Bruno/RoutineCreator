from .excerciseSeed import SeedExcercise

class Seed:
    def __init__(self, conn):
        self.conn = conn

    def init(self):
        try:
            print("Iniciando Seed")
            SeedExcercise(self.conn).run()
            print("Las seeds se cargaron correctamente")
        except:
            raise "Error en las seeds"



