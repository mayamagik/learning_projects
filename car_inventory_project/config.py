import os

# Absolute base directory (folder where config.py is located/ resolves to car_inventory_project

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Full path to  database file
DB_PATH = os.path.join(BASE_DIR, "db", "vehicle_fleet.db")