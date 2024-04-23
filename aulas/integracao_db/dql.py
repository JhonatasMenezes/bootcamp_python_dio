import sqlite3
from connection import conn

cursor = conn.cursor()
cursor.row_factory = sqlite3.Row


def fetch_by_id(cursor, id):
    return cursor.execute(
        "SELECT * FROM  clientes WHERE id =?", 
        (id,)
        ).fetchone()


def fetch_all(cursor):
    results = cursor.execute(
        "SELECT * FROM clientes"
        ).fecthall()
    return [row for row in results]

