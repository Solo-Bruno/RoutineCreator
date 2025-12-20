import psycopg2

def createExcercise(conn, cursor):
    TableExercise = """
    CREATE TABLE IF NOT EXISTS Exercise (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    type VARCHAR(255),
    img VARCHAR(255)
    );
    """
    try:
        cursor.execute(TableExercise)
        conn.commit()
        print("✅ Table created Exercise successfully.")
    except (Exception, psycopg2.Error) as error:
        print(error)
        conn.rollback()
        raise


def createRoutineTable(conn, cursor):
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
        raise

def createDayTable(conn, cursor):
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
        raise

def createTableDayExercise(conn, cursor):
    DayExercise = """  
    CREATE TABLE IF NOT EXISTS Day_Exercise (
        id SERIAL PRIMARY KEY,
        day_id INTEGER REFERENCES Day(id) ON DELETE CASCADE,
        exercise_id INTEGER REFERENCES Exercise(id) ON DELETE CASCADE,
        orden INTEGER 
    );
    """
    try:
        cursor.execute(DayExercise)
        conn.commit()
        print("✅ Table created DayExercise successfully.")
    except (Exception, psycopg2.Error) as error:
        print(f"❌ Error creating Set table: {error}")
        conn.rollback()
        raise

def createSetTable(conn, cursor):
    TableSet = """
    CREATE TABLE IF NOT EXISTS Set (
        id SERIAL PRIMARY KEY,
        cantidad INTEGER NOT NULL,
        repeticiones INTEGER NOT NULL,
    
        -- FK a la tabla intermedia
        day_exercise_id INTEGER REFERENCES Day_Exercise(id) ON DELETE CASCADE
    );
    """
    try:
        cursor.execute(TableSet)
        conn.commit()
        print("✅ Table created Set successfully.")
    except (Exception, psycopg2.Error) as error:
        print(f"❌ Error creating Set table: {error}")
        conn.rollback()
        raise

def initialization(conn, cursor):
    try:
        createExcercise(conn, cursor)
        createRoutineTable(conn, cursor)
        createDayTable(conn, cursor)
        createTableDayExercise(conn, cursor)
        createSetTable(conn, cursor)
    except (Exception, psycopg2.Error) as error:
        cursor.close()
        conn.close()
        raise error

