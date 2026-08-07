import sqlite3
conn=sqlite3.connect('tasks.db')
cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS
tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
completed INTEGER DEFAULT 0)''')
print('done!')

def get_db_connection():
    """Helper function to get a database connection with dictionary-like row access."""
    conn=sqlite3.connect("tasks.db")
    conn.row_factory=sqlite3.Row
    return conn
