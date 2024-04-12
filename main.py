from database_connection import DatabaseConnection

databaseConnection = DatabaseConnection()


################################### GENERAL FUNCTIONS ###################################

def register_user():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    date_of_birth = input("Date of Birth: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    while password != confirm_password:
        print("Passwords do not match")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")
    if databaseConnection.register_user(email, password, first_name, last_name, date_of_birth):
        print("Successfully registered")
    else:
        print("Failed to register")


################################### USER FUNCTIONS ###################################
def user_login():
    print("User Login")
    email = input("Email: ")
    password = input("Password: ")
    return databaseConnection.login_as_user(email, password)


def user_functions():
    user_id = user_login()
    if not user_id:
        print("Failed to login")
        return

    choice = None
    while choice != "q":
        print("User functions:")
        print("1 - Profile Management")
        print("2 - Dashboard")
        print("3 - Schedule Management")
        print("q - Logout")
        choice = input(">>>")

        if choice == "1":
            profile_management(user_id)
        elif choice == "2":
            dashboard(user_id)
        elif choice == "3":
            user_schedule_management(user_id)


def profile_management(user_id):
    choice = None
    while choice != "q":
        print("User Schedule Management Functions:")
        print("1 - Update personal information")
        print("2 - Update fitness goals")
        print("3 - Update health metrics")
        print("4 - Update password")
        print("q - Logout")

        choice = input(">>>")

        if choice == "1":
            print("Please enter your personal information")
            email = input("Email: ")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            date_of_birth = input("Date of birth(yyyy-mm-dd): ")
            databaseConnection.update_user(user_id, email, first_name, last_name, date_of_birth)
        if choice == "2":
            pass
        if choice == "3":
            pass
        if choice == "4":
            pass



def dashboard(user_id):
    pass


def user_schedule_management(user_id):
    print("User Schedule Management Functions:")
    print("1 - Schedule training sessions")
    print("2 - view training sessions")
    print("3 - Cancel training session")
    print("4 - Schedule training sessions")
    print("5 - view training sessions")
    print("6 - Cancel training session")
    print("q - Back")

    choice = input(">>>")
    while choice != "q":
        if choice == "1":
            pass
        if choice == "2":
            pass
        if choice == "3":
            pass
        if choice == "4":
            pass
        if choice == "5":
            pass
        if choice == "6":
            pass



################################### TRAINER FUNCTIONS ###################################
def trainer_login():
    print("Trainer Login")
    email = input("Email: ")
    password = input("Password: ")
    return databaseConnection.login_as_trainer(email, password)


def trainer_functions():
    trainer_id = trainer_login()
    if not trainer_id:
        print("Failed to login")
        return

    choice = None
    while choice != "q":
        print("1 - Schedule Management")
        print("2 - Member Profile Viewing")
        print("q - Quit")
        choice = input(">>>")

        if choice == "1":
            trainer_schedule_management(trainer_id)
        if choice == "2":
            member_profile_viewing(trainer_id)



def trainer_schedule_management(trainer_id):
    choice = None
    while choice != "q":
        print("\nTrainer Schedule Management Functions:")
        print("1 - View available times")
        print("2 - Add timeslot to available times")
        print("3 - Delete timeslot from available times")
        print("4 - Cancel training session")
        print("q - Back")

        choice = input(">>>")

        if choice == "1":
            times = databaseConnection.view_available_trainer_times(trainer_id)
            print("Times:")
            for time in times:
                print(time[0].strftime("%H:%M"))
            input("Press enter to continue...")
        if choice == "2":
            time = input("Please enter time slot you wish to add(HH in 24h format): ")
            if(databaseConnection.add_available_trainer_times(trainer_id, time)):
                print("Time slot added")
            else:
                print("Failed to add time slot")
        if choice == "3":
            time = input("Please enter time slot you wish to delete (HH in 24h format): ")
            if (databaseConnection.delete_available_trainer_times(trainer_id, time)):
                print("Time slot deleted")
            else:
                print("Failed to delete time slot")
        if choice == "4":
            pass

def member_profile_viewing():
    pass


################################### ADMIN FUNCTIONS ###################################
def admin_login():
    print("Admin Login")
    email = input("Email: ")
    password = input("Password: ")
    return databaseConnection.login_as_admin(email, password)


def admin_functions():
    admin_id = admin_login()
    if not admin_id:
        print("Failed to login")
        return

    choice = None
    while choice != "q":
        print("1 - Room Booking Management")
        print("2 - Equipment Maintenance Monitoring")
        print("3 - Class Schedule Updating")
        print("4 - Billing and Payment Processing")
        print("q - Quit")
        choice = input(">>>")

        if choice == "1":
            room_booking_management(admin_id)
        if choice == "2":
            equipment_maintenance_monitoring(admin_id)
        if choice == "3":
            class_schedule_updating(admin_id)
        if choice == "4":
            bill_and_payment_processing(admin_id)


def room_booking_management():
    pass


def equipment_maintenance_monitoring():
    pass


def class_schedule_updating():
    print("Class Schedule Updating:")
    print("1 - Create class")
    print("2 - Update class schedule")
    print("3 - Cancel class")
    print("q - Back")
    choice = input(">>>")

    if choice == "q":
        return

    if choice == "1":
        room_booking_management()
    if choice == "2":
        equipment_maintenance_monitoring()
    if choice == "3":
        class_schedule_updating()
    if choice == "4":
        bill_and_payment_processing()


def bill_and_payment_processing():
    print("Billing and Payment:")
    print("1 - Create new invoice")
    print("2 - View bills")
    print("q - Back")
    choice = input(">>>")

    if choice == "q":
        return

    if choice == "1":
        room_booking_management()
    if choice == "2":
        equipment_maintenance_monitoring()




################################### MAIN ###################################

if __name__ == "__main__":
    print("Health and Fitness Club login")

    choice = None
    while choice != "q":
        print("\n1 - Authenticate as User")
        print("2 - Authenticate as Trainer")
        print("3 - Authenticate as Admin")
        print("4 - Register for User account")
        print("q - Quit")

        choice = input(">>>")

        if choice == "1":
            user_functions()
        elif choice == "2":
            trainer_functions()
        elif choice == "3":
            admin_functions()
        elif choice == "4":
            register_user()
