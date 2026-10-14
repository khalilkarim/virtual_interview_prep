import sqlite3

from flask import jsonify


# conn.row_factory =sqlite3.Row


def init_db():
    conn = sqlite3.connect("coach.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS answers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL)""")
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect("coach.db")
    conn.row_factory = sqlite3.Row
    return conn


