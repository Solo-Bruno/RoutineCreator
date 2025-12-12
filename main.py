import connection as connection
import tables

def main():
    conn = connection.getConnection()
    cursor = conn.cursor()


    "Init tables"
    #tables.initialization(conn, cursor)



if __name__ == "__main__":
    main()