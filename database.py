import sqlite3 # Use the functionality provided by sqlite3 module

def get_observations(): # The SELECT operation
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM observations")
    observations = cursor.fetchall()
    print(dict(observations[0]))
    connection.close()
    return observations


def add_observation(observation): # The INSERT operation
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO observations (species, confidence, date, location, image)
    VALUES (?, ?, ?, ?, ?)""", (observation["species"], observation["confidence"], observation["date"], observation["location"],
                                observation["image"]))
    # ? are parameterised placeholders
    connection.commit() # commits the newly inserted row to the SQLite database file so that it persists on the disk
    row_id = cursor.lastrowid
    connection.close()
    return row_id

def get_connection():
    connection = sqlite3.connect("fauna.db")
    connection.row_factory = sqlite3.Row
    return connection

def initialise_database():
    connection = get_connection()
    cursor = connection.cursor() # Cursor is like a messenger
    cursor.execute("""CREATE TABLE IF NOT EXISTS observations (
    obs_id INTEGER PRIMARY KEY,
    species TEXT,
    confidence REAL,
    date TEXT,
    location TEXT,
    image TEXT
    );""") # if not exists part ensures code does not crash if we already have fauna.db
    connection.commit()
    connection.close()
