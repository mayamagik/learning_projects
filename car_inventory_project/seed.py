# db/seed.py

import sqlite3
import csv

DB_PATH = "db/vehicle_fleet.db"
CSV_PATH = "data/cars.csv"

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    
    with open(CSV_PATH, newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:

 # Check if license_plate already exists

            cursor.execute("SELECT 1 FROM vehicles WHERE license_plate = ?", (row['license_plate'],))
            if cursor.fetchone() is None:
                cursor.execute("""
                INSERT INTO vehicles (type, make, model, hp, num_seats, max_kmh, year, license_plate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                row['type'],
                row['make'],
                row['model'],
                int(row['hp']),           # convert to int
                int(row['num_seats']),    # convert to int
                int(row['max_kmh']),      # convert to int
                int(row['year']),         # convert to int
                row['license_plate'],
                ))
                
            else:
                print(f"Skipping duplicate license_plate: {row['license_plate']}")

    conn.commit()
                  
                       
                       