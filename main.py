import json

BOOKINGS_FILE = 'bookings.json'

# Loading data from JSON
def load_bookings():
    with open(BOOKINGS_FILE, 'r') as file:
        return json.load(file)

# Saving data to JSON
def save_bookings(bookings):
    with open(BOOKINGS_FILE, 'w') as file:
        json.dump(bookings, file, indent=4)

# Add booking method
def add_booking(guest_name, room_number, check_in_date, check_out_date):
    bookings = load_bookings()
    new_booking = {
        'guest_name': guest_name,
        'room_number': room_number,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date
    }
    bookings.append(new_booking)
    save_bookings(bookings)
    print(f"Booking added for {guest_name} in room {room_number}.")

# View booking method
def view_bookings():
    bookings = load_bookings()
    if not bookings:
        print("No bookings found.")
        return
    for booking in bookings:
        print(f"Guest: {booking['guest_name']}, Room: {booking['room_number']}, Check-in: {booking['check_in_date']}, Check-out: {booking['check_out_date']}")

# Main menu options
def main():
    while True:
        print("\nHotel Booking System")
        print("1. Add Booking")
        print("2. View Bookings")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            guest_name = input("Enter guest name: ")
            room_number = input("Enter room number: ")
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            add_booking(guest_name, room_number, check_in_date, check_out_date)
        elif choice == '2':
            view_bookings()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()