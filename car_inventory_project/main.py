from car_logic import get_vehicle_data, add_more_cars, print_vehicles
import data_access

def main():
    while True:
        print("\nMenu:")
        print("1. Add new vehicle")
        print("2. View all vehicles")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            vehicle = get_vehicle_data()
            data_access.insert_vehicle(*vehicle)
            print("Vehicle added successfully!")

        elif choice == "2":
            vehicles = data_access.fetch_all_vehicles()
            print_vehicles(vehicles)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

