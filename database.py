import sqlite3 # Use the functionality provided by sqlite3 module

connection = sqlite3.connect("fauna.db")
cursor = connection.cursor() # Cursor is like a messenger
cursor.execute("""CREATE TABLE IF NOT EXISTS observations (
    obs_id INTEGER PRIMAY KEY,
    species TEXT,
    confidence REAL,
    date TEXT,
    location TEXT,
    image TEXT
);""") # if not exists part ensures code does not crash if we already have fauna.db
connection.commit()
connection.close()

