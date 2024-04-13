from database_connection import DatabaseConnection
import print_functions as p
import support_functions as s

# database connection object
conn = DatabaseConnection()

def admin_login():
    print("Admin Login")
    email = input("Email: ")
    password = input("Password: ")
    return conn.login_as_admin(email, password)

def view_room_bookings():
    bookings = conn.get_room_bookings()
    if bookings:
        p.print_bookings(bookings)
    else:
        print("No bookings")

def book_room():
    print("Available rooms:")
    rooms = conn.get_rooms()
    if rooms:
        p.print_rooms(rooms)
    else:
        print("No rooms available")
        return
    room_index = int(input("Enter room id you wish to book: "))
    class_id = input("Enter class id if this booking is for a class: ")
    if class_id == "":
        class_id = None
    date = input("Enter date of booking: ")
    time = s.get_time_from_user("Enter booking time: ")
    info = input("Enter booking information: ")

    if conn.add_room_booking(rooms[room_index][0], class_id, date, time, info):
        print("Successfully added booking")
    else:
        print("Failed to add booking")

def update_booking():
    bookings = conn.get_room_bookings()
    if bookings:
        p.print_bookings(bookings)
    else:
        print("No bookings")
        return
    booking_index = int(input("Enter index of booking to update: "))
    date = input("Enter date of booking: ")
    time = s.get_time_from_user("Enter booking time:")

    if conn.bookings_exists(bookings[booking_index][1], date, time):
        print("Room is taken at this time")
        return

    if conn.update_room_booking(bookings[booking_index][0], date, time):
        print("Successfully updated booking")
    else:
        print("Failed to update booking")

def delete_booking():
    bookings = conn.get_room_bookings()
    if bookings:
        p.print_bookings(bookings)
    else:
        print("No bookings")
        return
    booking_index = int(input("Enter index of booking to cancel: "))

    if conn.delete_room_booking(bookings[booking_index][0]):
        print("Booking successfully cancelled")
    else:
        print("Failed to cancel booking")

def view_equipment():
    equipment = conn.get_equipment_info()
    if equipment:
        p.print_equipment(equipment)
    else:
        print("No equipment")

def update_maintenance_date():
    equipment = conn.get_equipment_info()
    if equipment:
        p.print_equipment(equipment)
    else:
        print("No equipment")
        return
    equipment_index = int(input("Enter the index of equipment to update: "))
    maintenance_date = input("Enter the new maintenance date(yyyy-mm-dd): ")

    equipment_id = equipment[equipment_index][0]
    if conn.update_equipment_maintenance_date(equipment_id, maintenance_date):
        print("Successfully updated maintenance date")
    else:
        print("Failed to update maintenance date")

def view_classes():
    print("Class list:")
    classes = conn.get_class_list()
    if classes:
        p.print_classes(classes)
    else:
        print("No classes")

def update_class_schedule():
    print("Class list:")
    classes = conn.get_class_list()
    if classes:
        p.print_classes(classes)
    else:
        print("No classes")
        return

    class_index = int(input("Enter class index: "))
    date = input("Enter new date: ")
    time = s.get_time_from_user("Enter new time: ")

    if conn.update_class_schedule(classes[class_index][0], date, time):
        print("Successfully updated class")
    else:
        print("Failed to update class")

def view_bills():
    bills = conn.get_bills()
    if bills:
        p.print_bills(bills)
    else:
        print("No bills")

def create_bill():
    email = input("Please enter the user's email: ")
    data = conn.search_user_by_email(email)
    if not data:
        print("No user found")
        return

    user_id = data[0][0]
    amount = input("Amount: ")
    date = input("Date: ")
    status = 'UNPAID'

    if conn.add_bill(user_id, date, amount, status):
        print("Bill successfully issued")
    else:
        print("Failed to generate bill")
