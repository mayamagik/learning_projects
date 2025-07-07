# car_logic.py

from tabulate import tabulate
from input_utils import get_valid_name, get_valid_numbers


def get_vehicle_data():
    print("Type your vehicle data:")
    type_ = get_valid_name("Type (Car, Truck, Motorbike): ")
    make = get_valid_name("Make: ")
    model = get_valid_name("Model: ")
    hp = get_valid_numbers("HP: ", 100, 400, "Pick a number 100-400")
    num_seats = get_valid_numbers("Number of Seats: ", 2, 6, "Pick a number 2-6")
    max_kmh = get_valid_numbers("Max km/h: ", 120, 300, "Pick a number between 120 and 300")
    year = get_valid_numbers("Year: ", 1900, 2025, "Pick a valid year")
    license_plate = input("License Plate: ")
    return (type_, make, model, hp, num_seats, max_kmh, year, license_plate)

def add_more_cars():
    return input("Would you like to add another vehicle? (y/n): ").lower() == "y"

def print_vehicles(vehicles):
    headers = ["No.", "Type", "Make", "Model", "HP", "Seats", "Max km/h", "Year", "License Plate"]
    rows = [(i + 1, *car[1:]) for i, car in enumerate(vehicles)]
    # cars from DB probably have id at index 0, so slice from 1 to get rest
    print(f"\nYou have {len(vehicles)} entries in your vehicle list.\n")
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

