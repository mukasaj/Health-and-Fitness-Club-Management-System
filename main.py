import datetime
from database_connection import DatabaseConnection

conn = DatabaseConnection()


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
    if conn.register_user(email, password, first_name, last_name, date_of_birth):
        print("Successfully registered")
    else:
        print("Failed to register")

def wait():
    input("Press enter to continue...")
def get_time_from_user(prompt):
    # acceptable time inputs
    times = ["00:00", "01:00", "02:00", "30:00", "4:00", "5:00", "6:00", "7:00", "8:00",
             "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
             "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]
    time = input(prompt)
    while time not in times:
        print("Invalid input. Format is 24h and HH:MM, all times must be on the hour (e.g 11:00)")
        time = input(prompt)
    return time

def map_python_weekday_to_string(weekday):
    if weekday == 0:
        return "MONDAY"
    elif weekday == 1:
        return "TUESDAY"
    elif weekday == 2:
        return "WEDNESDAY"
    elif weekday == 3:
        return "THURSDAY"
    elif weekday == 4:
        return "FRIDAY"
    elif weekday == 5:
        return "SATURDAY"
    elif weekday == 6:
        return "SUNDAY"


################################### USER FUNCTIONS ###################################
def user_login():
    print("User Login")
    email = input("Email: ")
    password = input("Password: ")
    return conn.login_as_user(email, password)


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
        print("2 - Manage fitness goals")
        print("3 - Manage health metrics")
        print("4 - Manage exercise routines")
        print("5 - Manage fitness Achievements")
        print("6 - Update password")
        print("q - Back")

        choice = input(">>>")

        if choice == "1":
            print("Please enter your personal information")
            email = input("Email: ")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            date_of_birth = input("Date of birth(yyyy-mm-dd): ")
            if conn.update_user(user_id, email, first_name, last_name, date_of_birth):
                print("Successfully updated personal information")
            else:
                print("Failed to update personal information")
        if choice == "2":
            manage_fitness_goals(user_id)
        if choice == "3":
            manage_health_metrics(user_id)
        if choice == "4":
            manager_exercise_routines(user_id)
        if choice == "5":
            manager_fitness_achievements(user_id)
        if choice == "6":
            print("Please enter your new password")
            password = input("Password: ")
            confirm_password = input("Confirm Password: ")
            while password != confirm_password:
                print("Passwords do not match")
                password = input("Password: ")
                confirm_password = input("Confirm Password: ")
            conn.update_user_password(user_id, password)


def print_goals(goals):
    goal_index = 0
    if goals:
        for goal in goals:
            print("{} - {}".format(goal_index, goal))
            goal_index += 1


def manage_fitness_goals(user_id):
    choice = None
    while choice != "q":
        print("Fitness goals:")
        print("1 - View fitness goals")
        print("2 - Add fitness goal")
        print("4 - Update fitness goal")
        print("4 - Delete fitness goal")
        print("q - Back")
        choice = input(">>>")

        if choice == "1":
            goals = conn.get_fitness_goals(user_id)
            if goals:
                print_goals(goals)
            else:
                print("You have no fitness goals")
            input("Press enter to continue...")
        if choice == "2":
            goal = input("Please enter your goal: ")
            if conn.add_fitness_goal(user_id, goal):
                print("Successfully added fitness goal")
            else:
                print("Failed to add fitness goal")
            input("Press enter to continue...")
        if choice == "3":
            goals = conn.get_fitness_goals(user_id)
            if goals:
                print_goals(goals)
            else:
                print("You have no fitness goals")
                input("Press enter to continue...")
                continue
            index_to_delete = int(input("Enter the index of the goal you want to update: "))
            new_goal = input("Please enter your new goal: ")
            old_goal = goals[index_to_delete][0]
            if conn.update_fitness_goal(user_id, old_goal, new_goal):
                print("Goal successfully updated")
            else:
                print("Failed to update goal")
        if choice == "4":
            goals = conn.get_fitness_goals(user_id)
            if goals:
                print_goals(goals)
            else:
                print("You have no fitness goals")
                input("Press enter to continue...")
                continue
            index_to_delete = int(input("Enter the index of the goal you want to delete: "))
            goal = goals[index_to_delete][0]
            if conn.delete_fitness_goal(user_id, goal):
                print("Goal successfully deleted")
            else:
                print("Failed to delete goal")


def manage_health_metrics(user_id):
    choice = None
    while choice != "q":
        print("Health metrics:")
        print("1 - View health metrics")
        print("2 - Update health metrics")
        print("q - Back")
        choice = input(">>>")

        if choice == "1":
            print("Health metrics:")
            metrics = conn.get_health_metrics(user_id)
            if metrics:
                for metric in metrics:
                    print(metric)
            else:
                print("You have no health metrics")
            input("Press enter to continue...")
        if choice == "2":
            height = input("Height: ")
            weight = input("Weight: ")
            if conn.update_health_metrics(user_id, height, weight):
                print("Successfully updated health metrics")
            else:
                print("Failed to update health metrics")
            input("Press enter to continue...")


def print_exercise_routines(exercises):
    exercise_index = 0
    for exercise in exercises:
        print("{} - {}".format(exercise_index, exercise))
        exercise_index += 1


def manager_exercise_routines(user_id):
    choice = None
    while choice != "q":
        print("Health metrics:")
        print("1 - View my exercises routines")
        print("2 - Add an exercise routine")
        print("3 - Update an exercise routine")
        print("4 - Delete an exercise routine")
        print("q - Back")
        choice = input(">>>")

        if choice == "1":
            exercises = conn.get_exercise_routines(user_id)
            if exercises:
                print_goals(exercises)
            else:
                print("You have no exercise routines")
            input("Press enter to continue...")
        if choice == "2":
            exercises = input("Enter exercise routine: ")
            if conn.add_exercise_routine(user_id, exercises):
                print("Added exercise routine")
            else:
                print("Failed to add exercise routine")
        if choice == "3":
            exercises = conn.get_exercise_routines(user_id)
            if exercises:
                print_goals(exercises)
            else:
                print("You have no exercise routines")
                input("Press enter to continue...")
                continue
            exercises_index = int(input("Enter exercise index you wish to update: "))
            old_exercise = exercises[exercises_index][0]
            new_exercise = input("Enter updated exercise: ")
            if conn.update_exercise_routines(user_id, old_exercise, new_exercise):
                print("Exercise routine successfully updated")
            else:
                print("Failed to update exercise routine")

        if choice == "4":
            exercises = conn.get_exercise_routines(user_id)
            if exercises:
                print_goals(exercises)
            else:
                print("You have no exercise routines")
                input("Press enter to continue...")
                continue
            exercises_index = int(input("Enter exercise index you wish to delete:"))
            exercise = exercises[exercises_index][0]
            if conn.delete_exercise_routine(user_id, exercise):
                print("Exercise routine successfully deleted")
            else:
                print("Failed to delete exercise routine")


def print_fitness_achievements(achievements):
    achievement_index = 0
    for achievement in achievements:
        print("{} - {}".format(achievement_index, achievement))
        achievement_index += 1


def manager_fitness_achievements(user_id):
    choice = None
    while choice != "q":
        print("Health metrics:")
        print("1 - View my achievement")
        print("2 - Add an achievement")
        print("3 - Update an achievement")
        print("4 - Delete an achievement")
        print("q - Back")
        choice = input(">>>")

        if choice == "1":
            achievements = conn.get_fitness_achievements(user_id)
            if achievements:
                print_fitness_achievements(achievements)
            else:
                print("You have no fitness achievements")
            input("Press enter to continue...")
        if choice == "2":
            achievement = input("Enter fitness achievement routine: ")
            if conn.add_fitness_achievements(user_id, achievement):
                print("Fitness achievement successfully added")
            else:
                print("Failed to add fitness achievement")
        if choice == "3":
            exercises = conn.get_fitness_achievements(user_id)
            if exercises:
                print_fitness_achievements(exercises)
            else:
                print("You have no fitness achievements")
                input("Press enter to continue...")
                continue
            achievement_index = int(input("Enter achievement index you wish to update: "))
            old_exercise = exercises[exercises_index][0]
            new_exercise = input("Enter updated achievement: ")
            if conn.update_fitness_achievements(user_id, old_exercise, new_exercise):
                print("Fitness achievement successfully updated!")
            else:
                print("Failed to update fitness achievement")

        if choice == "4":
            exercises = conn.get_fitness_achievements(user_id)
            if exercises:
                print_fitness_achievements(exercises)
            else:
                print("You have no fitness achievements")
                input("Press enter to continue...")
                continue
            exercises_index = int(input("Enter achievement index you wish to delete:"))
            exercise = exercises[exercises_index][0]
            if conn.delete_exercise_routine(user_id, exercise):
                print("Fitness achievement successfully deleted")
            else:
                print("Failed to delete fitness achievement")


def dashboard(user_id):
    exercises = conn.get_exercise_routines(user_id)
    achievements = conn.get_fitness_achievements(user_id)
    health_stats = conn.get_health_metrics(user_id)
    counter = 1

    print("DASHBOARD:")
    print("Your exercises are:")
    if exercises:
        for exercise in exercises:
            print("{} - {}".format(counter, exercise[0]))
            counter += 1
    else:
        print("No exercises found")
    print("\nYour achievements are:")
    counter = 1
    if achievements:
        for achievement in achievements:
            print("{} - {}".format(counter, achievement[0]))
            counter += 1
    else:
        print("No achievements found")
    print("\nYour health metrics:")
    print("Height: {}".format(health_stats[0][0]))
    print("Weight: {}".format(health_stats[0][1]))


def user_schedule_management(user_id):
    choice = None
    while choice != "q":
        print("User Schedule Management Functions:")
        print("1 - View training sessions schedule")
        print("2 - Schedule training sessions")
        print("3 - Cancel training session")
        print("4 - View class schedule")
        print("5 - Register for class")
        print("6 - Drop class")
        print("q - Back")

        choice = input(">>>")

        if choice == "1":
            sessions = conn.get_training_sessions(user_id)
            if sessions:
                print_fitness_achievements(sessions)
            else:
                print("You have no training sessions scheduled")
            input("Press enter to continue...")
        if choice == "2":
            trainers = conn.get_trainers();

            trainer_index = 0
            if trainers:
                for trainer in trainers:
                    print(f"{trainer_index} - {trainer}")
                    trainer_index += 1

            selected_trainer = int(input("Please into the index of the trainer you'd like to book a session with: "))

            trainer_id = trainers[selected_trainer][0]
            times = conn.get_trainer_times(trainer_id)
            if times:
                print("This trainer is available at these times")
                for time in times:
                    print(f"Day: {time[0]} - Time: {time[1]}")
            else:
                print("This trainer has no times available")
                input("Press enter to continue...")
                continue

            date = input("Please enter you session date: ")
            time = input("Please enter you session time: ")
            weekday = map_python_weekday_to_string(datetime.datetime.strptime(date, "%Y-%m-%d").weekday())
            mapped_time = datetime.datetime.strptime(time, '%H:%M').time()
            print((str(weekday).upper(), time))
            if (str(weekday).upper(), mapped_time) not in times:
                print(f"This trainer is not available at {time} on {weekday}")
                continue

            if conn.trainer_is_busy(trainer_id, date, time):
                print(f"This trainer is not available at {time} on {date}")
                continue

            session_info = "Please enter the session info: "
            if conn.schedule_training_session(user_id, trainer_id, date, time, session_info):
                print("Successfully scheduled training session")
            else:
                print("Failed to schedule training session")

        if choice == "3":
            sessions = conn.get_training_sessions(user_id)
            if sessions:
                print_fitness_achievements(sessions)
            else:
                print("You have no training sessions scheduled")
                input("Press enter to continue...")
                continue
            session_index = int(input("Enter session index you wish to delete:"))
            session_id = sessions[session_index][0]

            if conn.delete_training_session(session_id):
                print("Successfully canceled training session")
            else:
                print("Failed to canceled training session")
        if choice == "4":
            classes = conn.get_registered_classes(user_id)
            if classes:
                print("Registered classes:")
                for cls in classes:
                    print(cls)
            else:
                print("You are not registered for any classes.")
            input("Press enter to continue...")
        if choice == "5":
            # printing classes available for registration
            print("Available classes:")
            classes = conn.get_class_list()
            for cls in classes:
                print(cls)
            class_id = input("Enter the class id of the class you wish to sign up for:")
            if conn.register_for_class(user_id, class_id):
                print("Successfully registered for class")
            else:
                print("Failed to register for class")
            input("Press enter to continue...")

        if choice == "6":
            classes = conn.get_registered_classes(user_id)
            if classes:
                print("Registered classes:")
                for cls in classes:
                    print(cls)
            else:
                print("You are not registered for any classes.")
                input("Press enter to continue...")
                continue
            class_id = input("Enter the class id of the class you wish to drop:")
            if conn.drop_class(user_id, class_id):
                print("Successfully dropped class")
            else:
                print("Failed to drop class")


################################### TRAINER FUNCTIONS ###################################
def trainer_login():
    print("Trainer Login")
    email = input("Email: ")
    password = input("Password: ")
    return conn.login_as_trainer(email, password)


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


def print_trainer_schedule(times):
    time_index = 0
    print("Times:")
    for time in times:
        print("{} - Day: {}, Time: {}".format(time_index, time[0], time[1].strftime("%H:%M")))
        time_index += 1


def trainer_schedule_management(trainer_id):
    choice = None
    while choice != "q":
        print("\nTrainer Schedule Management Functions:")
        print("1 - View available times")
        print("2 - Add timeslot to available times")
        print("3 - Delete timeslot from available times")
        print("q - Back")

        choice = input(">>>")

        if choice == "1":
            times = conn.view_available_trainer_times(trainer_id)
            if (times):
                print_trainer_schedule(times)
            else:
                print("No times set")
            input("Press enter to continue...")
        if choice == "2":
            day = input("Please enter the day: ")
            time = input("Please enter time slot(HH in 24h format): ")
            if (conn.add_available_trainer_times(trainer_id, day, time)):
                print("Time slot added")
            else:
                print("Failed to add time slot")
        if choice == "3":
            times = conn.view_available_trainer_times(trainer_id)
            if (times):
                print_trainer_schedule(times)
            else:
                print("No times set")
                input("Press enter to continue...")
                return

            index = int(input("Enter the index of the time slot you wish to delete: "))
            if (conn.delete_available_trainer_times(trainer_id, times[index][0], times[index][1])):
                print("Time slot deleted")
            else:
                print("Failed to delete time slot")
        if choice == "4":
            pass


def member_profile_viewing(trainer_id):
    choice = None
    while choice != "q":
        print("Trainer member viewing:")
        print("1 - Search for member using first and last name")
        print("2 - Search for member using email")
        choice = input(">>>")

        if choice == "1":
            first_name = input("Please enter the user's first name: ")
            last_name = input("Please enter the user's last name: ")
            data = conn.search_user_by_name(first_name, last_name)
            if data:
                print(data)
            else:
                print("No user found")
        if choice == "2":
            email = input("Please enter the user's email:")
            data = conn.search_user_by_email(email)
            if data:
                print(data)
            else:
                print("No user found")


################################### ADMIN FUNCTIONS ###################################
def admin_login():
    print("Admin Login")
    email = input("Email: ")
    password = input("Password: ")
    return conn.login_as_admin(email, password)


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
            room_booking_management()
        if choice == "2":
            equipment_maintenance_monitoring()
        if choice == "3":
            class_schedule_updating()
        if choice == "4":
            bill_and_payment_processing()

def print_rooms(rooms):
    room_index = 0
    for room in rooms:
        print("{} - {}".format(room_index, room))
        room_index += 1
def print_bookings(bookings):
    booking_index = 0
    for booking in bookings:
        print("{} - {}".format(booking_index, booking))
        booking_index += 1
def room_booking_management():
    choice = None
    while choice != "q":
        print("Room booking management:")
        print("1 - View rooming bookings")
        print("2 - Add rooming booking")
        print("3 - Updating rooming booking")
        print("4 - Delete rooming booking")
        
        choice = input(">>> ")
        
        if choice == "1":
            bookings = conn.get_room_bookings()
            if bookings:
                print_bookings(bookings)
            else:
                print("No bookings")
            wait()
        if choice == "2":
            print("Available rooms:")
            rooms = conn.get_rooms()
            if rooms:
                print_rooms(rooms)
            else:
                print("No rooms available")
                wait()
                continue
            room_index = int(input("Enter room id you wish to book: "))
            class_id = input("Enter class id if this booking is for a class: ")
            if class_id == "":
                class_id = None
            date = input("Enter date of booking: ")
            time = get_time_from_user("Enter booking time: ")
            info = input("Enter booking information: ")

            if conn.add_room_booking(rooms[room_index][0], class_id, date, time, info):
                print("Successfully added booking")
            else:
                print("Failed to add booking")

        if choice == "3":
            bookings = conn.get_room_bookings()
            if bookings:
                print_bookings(bookings)
            else:
                print("No bookings")
                wait()
                continue
            booking_index = int(input("Enter index of booking to update"))
            date = input("Enter date of booking: ")
            time = get_time_from_user("Enter booking time:")

            if conn.bookings_exists(bookings[booking_index][1], date, time):
                print("Room is taken at this time")
                wait()
                continue

            if conn.update_room_booking(bookings[booking_index][0], date, time):
                print("Successfully updated booking")
            else:
                print("Failed to update booking")

        if choice == "4":
            bookings = conn.get_room_bookings()
            if bookings:
                print_bookings(bookings)
            else:
                print("No bookings")
                wait()
                continue
            booking_index = int(input("Enter index of booking to cancel"))

            if conn.delete_room_booking(bookings[booking_index][0]):
                print("Booking successfully cancelled")
            else:
                print("Failed to cancel booking")

def print_equipment(equipment):
    equipment_index = 0
    for equip in equipment:
        print("{} - {}".format(equipment_index, equip))
        equipment_index += 1


def equipment_maintenance_monitoring():
    choice = None
    while choice != "q":
        print("Equipment Maintenance Monitoring")
        print("1 - View equipment maintenance dates")
        print("2 - Update equipment maintenance dates")

        # getting input from user
        choice = input(">>> ")

        if choice == "1":
            equipment = conn.get_equipment_info()
            if equipment:
                print_equipment(equipment)
            else:
                print("No equipment")
            input("Press enter to continue...")
        if choice == "2":
            equipment = conn.get_equipment_info()
            if equipment:
                print_equipment(equipment)
            else:
                print("No equipment")
                input("Press enter to continue...")
                continue
            equipment_index = int(input("Enter the index of equipment to update: "))
            maintenance_date = input("Enter the new maintenance date(yyyy-mm-dd): ")

            equipment_id = equipment[equipment_index][0]
            if conn.update_equipment_maintanance_date(equipment_id, maintenance_date):
                print("Successfully updated maintenance date")
            else:
                print("Failed to update maintenance date")

def print_classes(classes):
    class_index = 0
    for a_class in classes:
        print("{} - {}".format(class_index, a_class))
        class_index += 1
def class_schedule_updating():
    choice = None
    while choice != "q":
        print("Class Schedule Updating:")
        print("1 - View class list")
        print("2 - Update class schedule")
        print("q - Back")
        choice = input(">>>")

        if choice == "1":
            print("Class list:")
            classes = conn.get_class_list()
            if classes:
                print_classes(classes)
            else:
                print("No classes")
            wait()
        if choice == "2":
            print("Class list:")
            classes = conn.get_class_list()
            if classes:
                print_classes(classes)
            else:
                print("No classes")
            wait()

            class_index = int(input("Enter class index: "))
            date = input("Enter new date: ")
            time = get_time_from_user("Enter new time: ")

            if conn.update_class_schedule(classes[class_index][0], date, time):
                print("Successfully updated class")
            else:
                print("Failed to update class")

def print_bills(bills):
    for bill in bills:
        print(bill)

def bill_and_payment_processing():
    choice = None
    while choice != "q":
        print("Billing and Payment:")
        print("1 - View bills")
        print("2 - Create new invoice")
        print("q - Back")
        choice = input(">>>")

        if choice == "1":
            bills = conn.get_bills()
            if bills:
                print_bills(bills)
            else:
                print("No bills")
                wait()
                continue

        if choice == "2":
            user_id = input("User ID: ")
            amount = input("Amount: ")
            date = input("Date: ")
            status = 'UNPAID'

            if conn.add_bill(user_id, date, amount, status):
                print("Bill successfully issued")
            else:
                print("Failed to generate bill")



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
