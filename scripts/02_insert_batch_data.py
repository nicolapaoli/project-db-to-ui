import os
import names
from coolname import generate_slug
from random import randrange, choice
import psycopg2

DB_URL = os.environ["POSTGRES_URI"]


def insert_bulk():
    conn = None
    try:
        print("Connecting to PostgreSQL db..")
        conn = psycopg2.connect(DB_URL,  sslmode='require')

        n_users = randrange(8, 10)
        n_projects = randrange(10, 100)

        print(f"Generating {n_users} users and {n_projects} projects")

        categories = ["R&D", "Sales", "Marketing",
                      "Operations", "Business", "Management"]

        users = []
        for r in range(0, n_users):
            users.append(names.get_first_name())

        projects = []
        for p in range(0, n_projects):
            projects.append((" ".join(generate_slug(randrange(2, 3)).split('-')),
                            choice(categories), randrange(1, n_users)))

        insert_batch_users(conn, users)
        insert_batch_projects(conn, projects)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("DB Connection closed.")


def insert_batch_users(conn, users):

    print(f"Inserting {len(users)} to the users table")
    cur = conn.cursor()
    for user in users:
        cur.execute(f"INSERT INTO users (nickname) VALUES ('{user}')")
    conn.commit()
    cur.close()
    print("DONE")


def insert_batch_projects(conn, projects):
    """ insert a new user into the table """
    sql = """INSERT INTO projects(title, category, assigned_to)
            VALUES(%s, %s, %s);"""

    print(f"Inserting {len(projects)} to the projects table")
    cur = conn.cursor()
    cur.executemany(sql, projects)
    conn.commit()
    cur.close()


if __name__ == '__main__':
    insert_bulk()
