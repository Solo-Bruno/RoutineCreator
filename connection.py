import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class Connection:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DATABASE"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    conn.autocommit = True
