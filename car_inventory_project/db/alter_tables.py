# db/alter_tables.py

import sqlite3
import os
from config import DB_PATH  

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


# Example: add a 'color' column to vehicles
cursor.execute("ALTER TABLE vehicles ADD COLUMN color TEXT")

conn.commit()
conn.close()