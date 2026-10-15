import sqlite3

DB_PATH = "coach.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""CREATE TABLE IF NOT EXISTS answers 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     question_id INTEGER NOT NULL,
                     text TEXT NOT NULL)""")
    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
