# ============================================
#        BOYS HOSTEL MANAGEMENT SYSTEM
# ============================================

# Hostel Details
total_floors = 7
rooms_per_floor = 5
total_rooms = total_floors * rooms_per_floor

# Room Types and Fees
room_types = {
    3: {"price": 7000, "total": 1},
    4: {"price": 6500, "total": 2},
    5: {"price": 6000, "total": 2}
}

# Store Candidate Details
candidates = []

# Hostel Facilities
facilities = [
    "Wi-Fi",
    "Laundry",
    "CCTV Cameras",
    "TV",
    "Geyser"
]

# Weekly Food Menu
food_menu = {
    "Monday": "Idli, Rice, Dal, Chapati",
    "Tuesday": "Dosa, Rice, Sambar, Chicken Curry",
    "Wednesday": "Upma, Rice, Dal, Egg Curry",
    "Thursday": "Puri, Rice, Sambar, Chapati",
    "Friday": "Idli, Rice, Chicken Curry",
    "Saturday": "Dosa, Rice, Dal, Egg Curry",
    "Sunday": "Poori, Biryani, Sweet"
}


# Display Hostel Details
def display_hostel_details():
    print("\n========================================")
    print("       BOYS HOSTEL MANAGEMENT")
    print("========================================")
    print("Total Floors:", total_floors)
    print("Rooms Per Floor:", rooms_per_floor)
    print("Total Rooms:", total_rooms)


# Candidate Registration
def register_candidate():
    print("\n========== CANDIDATE REGISTRATION ==========")

    name = input("Enter candidate name: ").strip()
    candidate_id = input("Enter candidate ID: ").strip()
    age = int(input("Enter candidate age: "))

    print("\nAvailable Sharing Types:")
    print("3 Sharing - Rs.7000 per month")
    print("4 Sharing - Rs.6500 per month")
    print("5 Sharing - Rs.6000 per month")

    sharing = int(input("Enter your sharing type (3, 4, or 5): "))

    if sharing not in room_types:
        print("Invalid sharing type!")
        return

    # Calculate capacity
    capacity = sharing * room_types[sharing]["total"]

    # Count candidates who selected the same sharing type
    filled = sum(
        1 for candidate in candidates
        if candidate["sharing"] == sharing
    )

    # Check availability
    if filled >= capacity:
        print("Sorry! No space available for this sharing type.")
        return

    # Calculate monthly fee
    fee = room_types[sharing]["price"]

    # Store candidate information
    candidate = {
        "name": name,
        "candidate_id": candidate_id,
        "age": age,
        "sharing": sharing,
        "fee": fee
    }

    candidates.append(candidate)

    print("\nCandidate registered successfully!")
    print("Candidate Name:", name)
    print("Candidate ID:", candidate_id)
    print("Age:", age)
    print("Sharing Type:", sharing, "Sharing")
    print("Monthly Hostel Fee: Rs.", fee)


# Display Candidate Details
def display_candidates():
    print("\n========== REGISTERED CANDIDATES ==========")

    if not candidates:
        print("No candidates registered yet.")
        return

    for candidate in candidates:
        print("------------------------------------")
        print("Candidate Name:", candidate["name"])
        print("Candidate ID:", candidate["candidate_id"])
        print("Age:", candidate["age"])
        print("Sharing Type:", candidate["sharing"])
        print("Monthly Fee: Rs.", candidate["fee"])


# Display Room Availability
def display_room_availability():
    print("\n========== ROOM AVAILABILITY ==========")

    for sharing, details in room_types.items():

        capacity = sharing * details["total"]

        filled = sum(
            1 for candidate in candidates
            if candidate["sharing"] == sharing
        )

        available = capacity - filled

        print("\nSharing Type:", sharing, "Sharing")
        print("Number of Rooms:", details["total"])
        print("Total Capacity:", capacity)
        print("Filled Spaces:", filled)
        print("Available Spaces:", available)
        print("Monthly Fee: Rs.", details["price"])


# Display Weekly Food Menu
def display_food_menu():
    print("\n========== WEEKLY FOOD MENU ==========")

    for day, menu in food_menu.items():
        print(day, ":", menu)


# Display Hostel Facilities
def display_facilities():
    print("\n========== HOSTEL FACILITIES ==========")

    for facility in facilities:
        print("-", facility)


# Main Program
display_hostel_details()

while True:

    print("\n========================================")
    print("       BOYS HOSTEL MAIN MENU")
    print("========================================")
    print("1. Candidate Registration")
    print("2. Display Candidate Details")
    print("3. Check Room Availability")
    print("4. Display Weekly Food Menu")
    print("5. Display Hostel Facilities")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        register_candidate()

    elif choice == "2":
        display_candidates()

    elif choice == "3":
        display_room_availability()

    elif choice == "4":
        display_food_menu()

    elif choice == "5":
        display_facilities()

    elif choice == "6":
        print("\nThank you for using Boys Hostel Management System!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")