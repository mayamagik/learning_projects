# db/data_access.py

import sqlite3

DB_PATH = "db/vehicle_fleet.db"

def insert_vehicle(type_, make, model, hp, num_seats, max_kmh, year, license_plate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vehicles (type, make, model, hp, num_seats, max_kmh, year, license_plate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (type_, make, model, hp, num_seats, max_kmh, year, license_plate)
    )
    
    conn.commit()
    conn.close()     

def fetch_all_vehicles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehicles")
    rows = cursor.fetchall()
    conn.close()
    return rows

def fetch_journeys_for(license_plate):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM journey_log WHERE license_plate = ?", (license_plate,))
        journeys = cursor.fetchall()
    return journeys

def delete_vehicle_by_plate(license_plate):
    with sqlite3.connect("db/vehicle_fleet.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM vehicles WHERE license_plate = ?", (license_plate,))
        conn.commit()


