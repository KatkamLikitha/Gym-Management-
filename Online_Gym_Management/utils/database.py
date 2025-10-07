import sqlite3

DB_FILE = 'database/gym.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            membership TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_member(name, age, membership):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO members (name, age, membership) VALUES (?, ?, ?)', (name, age, membership))
    conn.commit()
    conn.close()

def get_members():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members')
    rows = cursor.fetchall()
    conn.close()
    return rows