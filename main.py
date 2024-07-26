import json

BOOKINGS_FILE = 'bookings.json'

# Loading data from JSON
def load_bookings():
    with open(BOOKINGS_FILE, 'r') as file:
        return json.load(file)


