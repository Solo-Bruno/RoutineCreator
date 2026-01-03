from modelo.exercise import Exercise
import psycopg2

exercises_to_insert = [
    # PECTORALES (17 items)
    ("PRESS PLANO (BARRA)", "PECTORALES", "img/PECTORALES/1.png"),
    ("PRESS PLANO (MANCUERNA)", "PECTORALES", "img/PECTORALES/2.png"),
    ("PRESS PLANO (MULTIPOWER)", "PECTORALES", "img/PECTORALES/3.png"),
    ("PRESS INCLINADO (BARRA)", "PECTORALES", "img/PECTORALES/4.png"),
    ("PRESS INCLINADO (MANCUERNA)", "PECTORALES", "img/PECTORALES/5.png"),
    ("PRESS INCLINADO (MULTIPOWER)", "PECTORALES", "img/PECTORALES/6.png"),
    ("PRESS DECLINADO (BARRA)", "PECTORALES", "img/PECTORALES/7.png"),
    ("PRESS DECLINADO (MANCUERNA)", "PECTORALES", "img/PECTORALES/8.jpg"),
    ("PRESS DECLINADO (MULTIPOWER)", "PECTORALES", "img/PECTORALES/9.png"),
    ("CONVERGENTE", "PECTORALES", "img/PECTORALES/10.webp"),
    ("APERTURAS (MANCUERNA)", "PECTORALES", "img/PECTORALES/11.webp"),
    ("APERTURAS (3 PLANOS)", "PECTORALES", "img/PECTORALES/12.webp"),
    ("PECK DECK", "PECTORALES", "img/PECTORALES/13.png"),
    ("CRUCES POLEA (DESDE ARRIBA)", "PECTORALES", "img/PECTORALES/14.png"),
    ("PULL OVER (MANCUERNA)", "PECTORALES", "img/PECTORALES/15.gif"),
    ("PRESS MÁQUINA", "PECTORALES", "img/PECTORALES/16.webp"),
    ("FONDOS PARALELAS", "PECTORALES", "img/PECTORALES/17.png"),

    # PIERNAS (37 items - Ajustado por el doble '24' en tu carpeta)
    ("SENTADILLAS (BARRA)", "PIERNAS", "img/PIERNAS/1.webp"),
    ("SENTADILLAS (MANCUERNA)", "PIERNAS", "img/PIERNAS/2.jpg"),
    ("SENTADILLAS (MULTIPOWER)", "PIERNAS", "img/PIERNAS/3.jpg"),
    ("SENTADILLAS (2 MANCUERNAS)", "PIERNAS", "img/PIERNAS/4.jpg"),
    ("SENTADILLAS FRONTALES (BARRA)", "PIERNAS", "img/PIERNAS/5.png"),
    ("SENTADILLA GOBLET", "PIERNAS", "img/PIERNAS/6.jpg"),
    ("SENTADILLA SUMO (BARRA)", "PIERNAS", "img/PIERNAS/7.jpg"),
    ("SENTADILLA SUMO (MANCUERNA)", "PIERNAS", "img/PIERNAS/8.jpg"),
    ("SENTADILLA SUMO (MULTIPOWER)", "PIERNAS", "img/PIERNAS/9.jpg"),
    ("SENTADILLA SUMO (2 MANCUERNAS)", "PIERNAS", "img/PIERNAS/10.jpg"),
    ("SISSY (BANCO)", "PIERNAS", "img/PIERNAS/11.webp"),
    ("SISSY (MANCUERNA)", "PIERNAS", "img/PIERNAS/12.webp"),
    ("SENTADILLAS LATERALES (BARRA)", "PIERNAS", "img/PIERNAS/13.jpg"),
    ("PRENSA 45º (BILATERAL)", "PIERNAS", "img/PIERNAS/14.jpg"),
    ("PRENSA 45º (UNILATERAL)", "PIERNAS", "img/PIERNAS/15.jpg"),
    ("PRENSA HACK (BILATERAL)", "PIERNAS", "img/PIERNAS/16.png"),
    ("PRENSA HACK (UNILATERAL)", "PIERNAS", "img/PIERNAS/17.png"),
    ("PRENSA HORIZONTAL (BILATERAL)", "PIERNAS", "img/PIERNAS/18.jpg"),
    ("PRENSA HORIZONTAL (UNILATERAL)", "PIERNAS", "img/PIERNAS/19.webp"),
    ("PRENSA VERTICAL", "PIERNAS", "img/PIERNAS/20.jpg"),
    ("TIJERAS O ESTOCADAS (BARRA)", "PIERNAS", "img/PIERNAS/21.gif"),
    ("TIJERAS O ESTOCADAS (MANCUERNAS)", "PIERNAS", "img/PIERNAS/22.jfif"),
    ("TIJERAS O ESTOCADAS (RUSA)", "PIERNAS", "img/PIERNAS/23.png"),
    ("TIJERAS O ESTOCADAS (MULTIPOWER)", "PIERNAS", "img/PIERNAS/24.gif"),
    ("BÚLGARAS (BARRA)", "PIERNAS", "img/PIERNAS/24.jfif"),  # Usando el segundo archivo 24
    ("BÚLGARAS (MANCUERNAS RUSA)", "PIERNAS", "img/PIERNAS/25.jfif"),
    ("BÚLGARAS (MULTIPOWER)", "PIERNAS", "img/PIERNAS/26.jfif"),
    ("PESO MUERTO RUMANO (BARRA)", "PIERNAS", "img/PIERNAS/27.jpg"),
    ("PESO MUERTO RUMANO (MANCUERNAS)", "PIERNAS", "img/PIERNAS/28.webp"),
    ("PESO MUERTO RUMANO (BARRA HEXAGONAL)", "PIERNAS", "img/PIERNAS/29.jpg"),
    ("PESO MUERTO SILLA CUADRICEPS", "PIERNAS", "img/PIERNAS/30.jpg"),
    ("CAMILLA FEMORAL ACOSTADO (RECORRIDOS PARCIALES)", "PIERNAS", "img/PIERNAS/31.png"),
    ("CAMILLA FEMORAL ACOSTADO (RECORRIDOS COMPLETOS)", "PIERNAS", "img/PIERNAS/32.png"),
    ("CAMILLA FEMORAL ACOSTADO (UNIPODAL)", "PIERNAS", "img/PIERNAS/33.png"),
    ("SILLA FEMORAL SENTADO (FEMORALERA)", "PIERNAS", "img/PIERNAS/34.png"),
    ("ADUCTORES (MÁQUINA)", "PIERNAS", "img/PIERNAS/35.webp"),
    ("CURL CUADRICEPS", "PIERNAS", "img/PIERNAS/36.png"),

    # GLÚTEOS (7 items)
    ("GLÚTEOS MÁQUINA (4 APOYOS)", "GLÚTEOS", "img/GLÚTEOS/1.gif"),
    ("GLÚTEOS POLEA PATADAS", "GLÚTEOS", "img/GLÚTEOS/2.jpg"),
    ("GLÚTEOS PUENTES (EN BANCO)", "GLÚTEOS", "img/GLÚTEOS/3.avif"),
    ("SUBIDAS A STEPS EN DESPLANTE", "GLÚTEOS", "img/GLÚTEOS/4.gif"),
    ("HIPEREXTENSIONES INVERTIDAS (HORIZONTAL)", "GLÚTEOS", "img/GLÚTEOS/5.avif"),
    ("PESO MUERTO PARA GLÚTEO", "GLÚTEOS", "img/GLÚTEOS/6.png"),
    ("PULL THROUGH", "GLÚTEOS", "img/GLÚTEOS/7.jpg"),

    # TRICEPS (12 items)
    ("JALONES POLEA PRONO", "TRICEPS", "img/TRICEPS/1.jpg"),
    ("JALONES TOMA INVERTIDA", "TRICEPS", "img/TRICEPS/2.jpg"),
    ("JALONES CUERDA", "TRICEPS", "img/TRICEPS/3.jpg"),
    ("MANCUERNA (A UNA MANO)", "TRICEPS", "img/TRICEPS/4.jpg"),
    ("MANCUERNA (A DOS MANOS)", "TRICEPS", "img/TRICEPS/5.jpg"),
    ("PATADAS DE BURRO", "TRICEPS", "img/TRICEPS/6.jpg"),
    ("POLEA A UNA MANO (HACIA ABAJO)", "TRICEPS", "img/TRICEPS/7.gif"),
    ("POLEA A UNA MANO (HORIZONTAL)", "TRICEPS", "img/TRICEPS/8.gif"),
    ("FONDOS BANCO", "TRICEPS", "img/TRICEPS/9.png"),
    ("FONDOS PARALELAS", "TRICEPS", "img/TRICEPS/10.png"),
    ("PRESS FRANCÉS", "TRICEPS", "img/TRICEPS/11.png"),
    ("PRESS CERRADO", "TRICEPS", "img/TRICEPS/12.png"),

    # ESPALDA (13 items - Saltando el archivo 10 que falta en tu carpeta)
    ("DOMINADAS (PRONO)", "ESPALDA", "img/ESPALDA/1.jpg"),
    ("DOMINADAS (SUPINO)", "ESPALDA", "img/ESPALDA/2.png"),
    ("JALONES AL PECHO (CERRADA)", "ESPALDA", "img/ESPALDA/3.jpg"),
    ("PESO MUERTO BÁSICO", "ESPALDA", "img/ESPALDA/4.png"),
    ("REMO CON BARRA (PRONO)", "ESPALDA", "img/ESPALDA/5.jpg"),
    ("REMO CON BARRA (SUPINO)", "ESPALDA", "img/ESPALDA/6.png"),
    ("REMO CON MANCUERNA (A 1 MANO)", "ESPALDA", "img/ESPALDA/7.jpg"),
    ("REMO CON MANCUERNA (A 2 MANOS)", "ESPALDA", "img/ESPALDA/8.jpg"),
    ("JALONES DE PIE", "ESPALDA", "img/ESPALDA/9.webp"),
    ("REMO ACOSTADO CON BARRA", "ESPALDA", "img/ESPALDA/11.jpg"),
    ("REMO BAJO CON POLEA (A 2 MANOS, PRONO)", "ESPALDA", "img/ESPALDA/12.png"),
    ("REMO BAJO CON POLEA (A 2 MANOS, NEUTRO)", "ESPALDA", "img/ESPALDA/13.png"),
    ("REMO BAJO CON POLEA (A 1 MANO)", "ESPALDA", "img/ESPALDA/14.jpg"),

    # BÍCEPS (11 items)
    ("CURL BARRA", "BÍCEPS", "img/BÍCEPS/1.png"),
    ("CURL BARRA W", "BÍCEPS", "img/BÍCEPS/2.png"),
    ("MARTILLO", "BÍCEPS", "img/BÍCEPS/3.png"),
    ("CURL POLEA BAJA (CON CUERDA)", "BÍCEPS", "img/BÍCEPS/4.png"),
    ("CURL POLEA BAJA (A 2 MANOS BARRA)", "BÍCEPS", "img/BÍCEPS/5.png"),
    ("BANCO SCOTT (CON BARRA)", "BÍCEPS", "img/BÍCEPS/6.gif"),
    ("BANCO SCOTT (A UNA MANO)", "BÍCEPS", "img/BÍCEPS/7.jpg"),
    ("POLEA ALTA (A 1 MANO)", "BÍCEPS", "img/BÍCEPS/8.jpg"),
    ("POLEA ALTA (A 2 MANOS)", "BÍCEPS", "img/BÍCEPS/9.jpg"),
    ("MANCUERNAS (A 2 MANOS, SENTADO)", "BÍCEPS", "img/BÍCEPS/10.jpg"),
    ("MANCUERNAS (A 2 MANOS, PARADO)", "BÍCEPS", "img/BÍCEPS/11.jpg"),

    # TRAPECIOS (1 - 3)
    ("ENCOGIMIENTOS (BARRA, DELANTERA)", "TRAPECIOS", "img/TRAPECIOS/1.webp"),
    ("ENCOGIMIENTOS (MANCUERNAS, DELANTERA)", "TRAPECIOS", "img/TRAPECIOS/2.jpg"),
    ("PARADO CON POLEA (MENTÓN)", "TRAPECIOS", "img/TRAPECIOS/3.png"),

    # ABDOMINALES (1 - 5)
    ("ELEVACIÓN TRONCO (PIES PISO)", "ABDOMINALES", "img/ABDOMINALES/1.png"),
    ("ELEVACIÓN DE PIERNAS (EN BANCO)", "ABDOMINALES", "img/ABDOMINALES/2.png"),
    ("ABDOMINALEA RUSAS", "ABDOMINALES", "img/ABDOMINALES/3.jpg"),
    ("DUMBBELL SIDE BEND", "ABDOMINALES", "img/ABDOMINALES/4.webp"),
]

class SeedExercise:
    def __init__(self, conn):
        self.conn = conn
    
    def run(self):
        ex = Exercise(self.conn)
        cant = ex.totales()
        try:
            if(cant == 0):
                img = ""
                for name, type in exercises_to_insert:
                    ex.inster(name, type, img)
            else:
                print("Las Seeds ya fueron ejecutadas correctamente")
        except psycopg2.Error as e:
            raise e
          



