import os
from sqlite3 import connect
import psycopg2

DB_URL = os.environ["POSTGRES_URI"]


def drop_tables():
    commands = (
        """
        DROP TABLE users CASCADE
        """,
        """
        DROP TABLE projects
        """
    )

    conn = None

    try:
        print("Connecting to PostgreSQL db..")
        conn = psycopg2.connect(DB_URL,  sslmode='require')
        cur = conn.cursor()

        print("Removing tables..")

        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("DB Connection closed.")


if __name__ == '__main__':
    drop_tables()
