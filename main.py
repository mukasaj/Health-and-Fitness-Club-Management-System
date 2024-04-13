import datetime
from database_connection import DatabaseConnection
import print_functions as p
import user_functions as u
import trainer_functions as t
import admin_functions as a
import support_functions as s

# database connection object
conn = DatabaseConnection()


################################### USER MENU FUNCTIONS ###################################

def user_functions():
    # user login
    user_id = u.user_login()
    if not user_id:
        print("Failed to login")
        return

    # user main menu
    choice = None
    while choice != "q":
        print("\nUser functions:")
        print("1 - Profile Management")
        print("2 - Dashboard")
        print("3 - Schedule Management")
        print("4 - Billing Menu")
        print("q - Logout")
        choice = input(">>> ")

        if choice == "1":
            profile_management(user_id)
        elif choice == "2":
            u.dashboard(user_id)
            s.wait()
        elif choice == "3":
            user_schedule_management(user_id)
        elif choice == "4":
            user_billing_management(user_id)


def profile_management(user_id):
    # profile management menu
    choice = None
    while choice != "q":
        print("\nUser profile management:")
        print("1 - Update personal information")
        print("2 - Manage fitness goals")
        print("3 - Manage health metrics")
        print("4 - Manage exercise routines")
        print("5 - Manage fitness Achievements")
        print("6 - Update password")
        print("q - Back")

        choice = input(">>> ")

        if choice == "1":
            u.update_personal_information(user_id)
            s.wait()
        if choice == "2":
            manage_fitness_goals(user_id)
        if choice == "3":
            manage_health_metrics(user_id)
        if choice == "4":
            manage_exercise_routines(user_id)
        if choice == "5":
            manage_fitness_achievements(user_id)
        if choice == "6":
            u.update_user_password(user_id)
            s.wait()


def manage_fitness_goals(user_id):
    # fitness goals management menu
    choice = None
    while choice != "q":
        print("\nFitness goals:")
        print("1 - View fitness goals")
        print("2 - Add fitness goal")
        print("3 - Update fitness goal")
        print("4 - Delete fitness goal")
        print("q - Back")
        choice = input(">>> ")

        if choice == "1":
            u.view_goals(user_id)
            s.wait()
        if choice == "2":
            u.add_user_goal(user_id)
            s.wait()
        if choice == "3":
            u.update_user_goal(user_id)
            s.wait()

        if choice == "4":
            u.delete_user_goal(user_id)
            s.wait()


def manage_health_metrics(user_id):
    # health metrics menu
    choice = None
    while choice != "q":
        print("\nHealth metrics:")
        print("1 - View health metrics")
        print("2 - Update health metrics")
        print("q - Back")
        choice = input(">>> ")

        if choice == "1":
            u.view_health_metrics(user_id)
            s.wait()
        if choice == "2":
            u.update_user_metric(user_id)
            s.wait()


def manage_exercise_routines(user_id):
    # exercise routine menu
    choice = None
    while choice != "q":
        print("\nExercise routines:")
        print("1 - View my exercises routines")
        print("2 - Add an exercise routine")
        print("3 - Update an exercise routine")
        print("4 - Delete an exercise routine")
        print("q - Back")
        choice = input(">>> ")

        if choice == "1":
            u.view_exercise_routines(user_id)
            s.wait()
        if choice == "2":
            u.add_exercise_routine(user_id)
            s.wait()
        if choice == "3":
            u.update_exercise_routine(user_id)
            s.wait()

        if choice == "4":
            u.delete_exercise_routine(user_id)
            s.wait()


def manage_fitness_achievements(user_id):
    # fitness achievements menu
    choice = None
    while choice != "q":
        print("\nFitness achievements:")
        print("1 - View my achievement")
        print("2 - Add an achievement")
        print("3 - Update an achievement")
        print("4 - Delete an achievement")
        print("q - Back")
        choice = input(">>> ")

        if choice == "1":
            u.view_achievements(user_id)
            s.wait()
        if choice == "2":
            u.add_achievement(user_id)
            s.wait()
        if choice == "3":
            u.update_achievement(user_id)
            s.wait()

        if choice == "4":
            u.delete_achievement(user_id)
            s.wait()


def user_schedule_management(user_id):
    # user schedule management menu
    choice = None
    while choice != "q":
        print("\nUser schedule management:")
        print("1 - View training sessions schedule")
        print("2 - Schedule training sessions")
        print("3 - Cancel training session")
        print("4 - View class schedule")
        print("5 - Register for class")
        print("6 - Drop class")
        print("q - Back")

        choice = input(">>> ")

        if choice == "1":
            u.view_training_sessions(user_id)
            s.wait()
        if choice == "2":
            u.schedule_training_session(user_id)
            s.wait()
        if choice == "3":
            u.cancel_training_session(user_id)
            s.wait()
        if choice == "4":
            u.view_classes(user_id)
            s.wait()
        if choice == "5":
            u.register_for_class(user_id)
            s.wait()
        if choice == "6":
            u.drop_class(user_id)
            s.wait()

def user_billing_management(user_id):
    # user schedule management menu
    choice = None
    while choice != "q":
        print("\nUser billing management:")
        print("1 - View my bills")
        print("2 - Pay a bill")
        print("q - Back")

        choice = input(">>> ")

        if choice == "1":
            u.view_bills(user_id)
            s.wait()
        if choice == "2":
            u.pay_bill(user_id)
            s.wait()



################################### TRAINER FUNCTIONS ###################################


def trainer_functions():
    # trainer login
    trainer_id = t.trainer_login()
    if not trainer_id:
        print("Failed to login")
        return

    # trainer main menu
    choice = None
    while choice != "q":
        print("\nTrainer functions:")
        print("1 - Schedule Management")
        print("2 - Member Profile Viewing")
        print("q - Quit")
        choice = input(">>> ")

        if choice == "1":
            trainer_schedule_management(trainer_id)
        if choice == "2":
            member_profile_viewing(trainer_id)


def trainer_schedule_management(trainer_id):
    # schedule management menu
    choice = None
    while choice != "q":
        print("\nTrainer Schedule Management Functions:")
        print("1 - View available times")
        print("2 - Add timeslot to available times")
        print("3 - Delete timeslot from available times")
        print("q - Back")

        choice = input(">>> ")

        if choice == "1":
            t.print_timeslots(trainer_id)
            s.wait()
        if choice == "2":
            t.add_timeslot(trainer_id)
            s.wait()
        if choice == "3":
            t.delete_timeslot(trainer_id)
            s.wait()


def member_profile_viewing(trainer_id):
    # member profile viewing menu
    choice = None
    while choice != "q":
        print("\nTrainer member viewing:")
        print("1 - Search for member using first and last name")
        print("2 - Search for member using email")
        choice = input(">>> ")

        if choice == "1":
            t.get_user_by_name()
            s.wait()
        if choice == "2":
            t.get_user_by_email()
            s.wait()


################################### ADMIN FUNCTIONS ###################################
def admin_functions():
    # admin login
    admin_id = a.admin_login()
    if not admin_id:
        print("Failed to login")
        return

    # admin main menu
    choice = None
    while choice != "q":
        print("\nAdmin functions:")
        print("1 - Room Booking Management")
        print("2 - Equipment Maintenance Monitoring")
        print("3 - Class Schedule Updating")
        print("4 - Billing and Payment Processing")
        print("q - Quit")
        choice = input(">>> ")

        if choice == "1":
            room_booking_management()
        if choice == "2":
            equipment_maintenance_monitoring()
        if choice == "3":
            class_schedule_updating()
        if choice == "4":
            bill_and_payment_processing()


def room_booking_management():
    # room booking menu
    choice = None
    while choice != "q":
        print("\nRoom booking management:")
        print("1 - View rooming bookings")
        print("2 - Add rooming booking")
        print("3 - Updating rooming booking")
        print("4 - Delete rooming booking")

        choice = input(">>> ")

        if choice == "1":
            a.view_room_bookings()
            s.wait()
        if choice == "2":
            a.book_room()
            s.wait()

        if choice == "3":
            a.update_booking()
            s.wait()

        if choice == "4":
            a.delete_booking()
            s.wait()


def equipment_maintenance_monitoring():
    # equipment maintenance menu
    choice = None
    while choice != "q":
        print("\nEquipment Maintenance monitoring")
        print("1 - View equipment maintenance dates")
        print("2 - Update equipment maintenance dates")
        print("q - Back")

        # getting input from user
        choice = input(">>> ")

        if choice == "1":
            a.view_equipment()
            s.wait()
        if choice == "2":
            a.update_maintenance_date()
            s.wait()


def class_schedule_updating():
    # class schedule updating menu
    choice = None
    while choice != "q":
        print("\nClass Schedule Updating:")
        print("1 - View class list")
        print("2 - Update class schedule")
        print("q - Back")
        choice = input(">>> ")

        if choice == "1":
            a.view_classes()
            s.wait()
        if choice == "2":
            a.update_class_schedule()
            s.wait()


def bill_and_payment_processing():
    # bill and payment processing menu
    choice = None
    while choice != "q":
        print("\nBilling and Payment:")
        print("1 - View bills")
        print("2 - Create new invoice")
        print("q - Back")
        choice = input(">>> ")

        if choice == "1":
            a.view_bills()
            s.wait()
        if choice == "2":
            a.create_bill()
            s.wait()


if __name__ == "__main__":
    # main menu used for login
    print("Health and Fitness Club login")

    choice = None
    while choice != "q":
        print("\n1 - Authenticate as User")
        print("2 - Authenticate as Trainer")
        print("3 - Authenticate as Admin")
        print("4 - Register for User account")
        print("q - Quit")

        choice = input(">>> ")

        if choice == "1":
            user_functions()
        elif choice == "2":
            trainer_functions()
        elif choice == "3":
            admin_functions()
        elif choice == "4":
            u.register_user()
