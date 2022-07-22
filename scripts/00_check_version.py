import os
import psycopg2

DB_URL = os.environ["POSTGRES_URI"]


def connect():
    conn = None
    try:
        print("Connecting to PostgreSQL db..")
        conn = psycopg2.connect(DB_URL,  sslmode='require')
        cur = conn.cursor()

        print('DB Version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("DB Connection closed.")


if __name__ == '__main__':
    connect()
