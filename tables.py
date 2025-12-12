import psycopg2

def createExcercise(conn, cursor):
    TableExercise = """
    CREATE TABLE IF NOT EXISTS Exercise (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    type VARCHAR(255)
    );
    """
    try:
        cursor.execute(TableExercise)
        conn.commit()
        print("✅ Table created Exercise successfully.")
    except (Exception, psycopg2.Error) as error:
        print(error)
        conn.rollback()


def createRoutineTable(conn, cursor):
    """Crea la tabla principal Routine."""
    TableRoutine = """
    CREATE TABLE IF NOT EXISTS Routine (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
    """
    try:
        cursor.execute(TableRoutine)
        conn.commit()
        print("✅ Table created Routine successfully.")
    except (Exception, psycopg2.Error) as error:
        print(f"❌ Error creating Routine table: {error}")
        conn.rollback()


def createDayTable(conn, cursor):
    """Crea la tabla Day (Días) con clave foránea a Routine (1:N)."""
    TableDay = """
    CREATE TABLE IF NOT EXISTS Day (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,

        -- FK a la tabla Routine
        routine_id INTEGER REFERENCES Routine(id) ON DELETE CASCADE
    );
    """
    try:
        cursor.execute(TableDay)
        conn.commit()
        print("✅ Table created Day successfully.")
    except (Exception, psycopg2.Error) as error:
        print(f"❌ Error creating Day table: {error}")
        conn.rollback()


def createSetTable(conn, cursor):
    """Crea la tabla Set (ejecuciones) con claves foráneas a Day y Exercise."""
    # Las columnas se renombran a 'cantidad' y 'repeticiones' para claridad.
    TableSet = """
    CREATE TABLE IF NOT EXISTS Set (
        id SERIAL PRIMARY KEY,
        cantidad INTEGER NOT NULL,
        repeticiones INTEGER NOT NULL,

        -- FK al día al que pertenece este set
        day_id INTEGER REFERENCES Day(id) ON DELETE CASCADE,

        -- FK al ejercicio que se realiza en este set
        exercise_id INTEGER REFERENCES Exercise(id) ON DELETE RESTRICT
    );
    """
    try:
        cursor.execute(TableSet)
        conn.commit()
        print("✅ Table created Set successfully.")
    except (Exception, psycopg2.Error) as error:
        print(f"❌ Error creating Set table: {error}")
        conn.rollback()

def initialization(conn, cursor):
    try:
        createExcercise(conn, cursor)
        createRoutineTable(conn, cursor)
        createDayTable(conn, cursor)
        createSetTable(conn, cursor)
    except (Exception, psycopg2.Error) as error:
        cursor.close()
        conn.close()

