import sqlite3
import sys

def initialize_database():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Create tables if they do not exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS events
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                           zone INTEGER,
                           event_type INTEGER,
                           data TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS zone_state
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                           zone INTEGER,
                           state INTEGER)''')

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
        sys.exit(1)