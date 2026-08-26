import sqlite3 # Use the functionality provided by sqlite3 module

def get_observations(): # The SELECT operation
    cursor.execute("SELECT * FROM observations")
    return cursor.fetchall()


def add_observation(observation): # The INSERT operation
    cursor.execute("""INSERT INTO observations (species, confidence, date, location, image)
    VALUES (?, ?, ?, ?, ?)""", (observation["species"], observation["confidence"], observation["date"], observation["location"],
                                observation["image"]))
    # ? are parameterised placeholders
    connection.commit() # commits the newly inserted row to the SQLite database file so that it persists on the disk
    return cursor.lastrowid


connection = sqlite3.connect("fauna.db")
connection.row_factory = sqlite3.Row
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


if __name__ == "__main__":
    # only run this when database.py is run directly
    test_observation = {
        "species": "Red Fox",
        "confidence": 0.91,
        "date": "17/08/26",
        "location": "Clapham",
        "image" : "fox.jpg"
    }

    add_observation(test_observation)
    results = get_observations()
    print(results)
    connection.close()