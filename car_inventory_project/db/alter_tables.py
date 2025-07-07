# db/alter_tables.py

import sqlite3

conn = sqlite3.connect("db/vehicle_fleet.db")
cursor = conn.cursor()

# Example: add a 'color' column to vehicles
cursor.execute("ALTER TABLE vehicles ADD COLUMN color TEXT")

conn.commit()
conn.close()