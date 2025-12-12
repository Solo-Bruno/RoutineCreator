import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def getConnection():
    try:
        parametros = {
            'user': os.getenv("DB_USER"),
            'password': os.getenv("DB_PASSWORD"),
            'host': os.getenv("DB_HOST"),
            'database': os.getenv("DB_DATABASE"),
        }

        connection = psycopg2.connect(**parametros)
        print("Connection established")
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)
