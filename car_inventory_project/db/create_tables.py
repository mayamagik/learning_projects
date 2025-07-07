# db/create_tables.py

import sqlite3
import os

# Get directory of the current script
base_dir = os.path.dirname(__file__)
db_path = os.path.join(base_dir, "vehicle_fleet.db")

conn = sqlite3.connect(db_path)
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
           
               
               