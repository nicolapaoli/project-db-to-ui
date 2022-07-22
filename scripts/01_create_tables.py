import os
from sqlite3 import connect
import psycopg2

DB_URL = os.environ["POSTGRES_URI"]


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            nickname VARCHAR NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS projects (
            project_id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            created_timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            assigned_to INTEGER NOT NULL,
            FOREIGN KEY (assigned_to)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )

    conn = None

    try:
        print("Connecting to PostgreSQL db..")
        conn = psycopg2.connect(DB_URL,  sslmode='require')
        cur = conn.cursor()

        print("Creating tables..")

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
    create_tables()
