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