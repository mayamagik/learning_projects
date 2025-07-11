# db/create_tables.py

import sqlite3
from config import DB_PATH  

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    make TEXT,
    model TEXT,
    hp INTEGER,
    num_seats INTEGER,
    max_kmh INTEGER,
    year INTEGER,
    license_plate TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS journey_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_plate TEXT,
    date TEXT,
    kilometer INTEGER,
    destination TEXT,
    private INTEGER
)
""")

conn.commit()
conn.close()
print("✅ Tables created and database initialized.")
           
               
               