import datetime
from database_connection import DatabaseConnection
import print_functions as p
import support_functions as s

# database connection object
conn = DatabaseConnection()


def trainer_login():
    print("Trainer Login")
    email = input("Email: ")
    password = input("Password: ")
    return conn.login_as_trainer(email, password)


def print_timeslots(trainer_id):
    times = conn.view_available_trainer_times(trainer_id)
    if (times):
        p.print_trainer_schedule(times)
    else:
        print("No times set")


def add_timeslot(trainer_id):
    day = input("Please enter the day: ")
    time = input("Please enter time slot(HH in 24h format): ")
    if (conn.add_available_trainer_times(trainer_id, day, time)):
        print("Time slot added")
    else:
        print("Failed to add time slot")


def delete_timeslot(trainer_id):
    times = conn.view_available_trainer_times(trainer_id)
    if (times):
        p.print_trainer_schedule(times)
    else:
        print("No times set")
        return

    index = int(input("Enter the index of the time slot you wish to delete: "))
    if (conn.delete_available_trainer_times(trainer_id, times[index][0], times[index][1])):
        print("Time slot deleted")
    else:
        print("Failed to delete time slot")

def get_user_by_name():
    first_name = input("Please enter the user's first name: ")
    last_name = input("Please enter the user's last name: ")
    data = conn.search_user_by_name(first_name, last_name)
    if data:
        print(data)
    else:
        print("No user found")
        return
    get_user_dashboard(data[0][0])

def get_user_by_email():
    email = input("Please enter the user's email:")
    data = conn.search_user_by_email(email)
    if data:
        print(data)
    else:
        print("No user found")
        return
    get_user_dashboard(data[0][0])

def get_user_dashboard(user_id):
    exercises = conn.get_exercise_routines(user_id)
    achievements = conn.get_fitness_achievements(user_id)
    health_stats = conn.get_health_metrics(user_id)

    print(" USER'S DASHBOARD:")
    print("User's exercises are:")
    if exercises:
        p.print_exercise_routines(exercises)
    else:
        print("No exercises found")
    print("\nUser's achievements are:")
    if achievements:
        p.print_fitness_achievements(achievements)
    else:
        print("No achievements found")
    print("\nYour health metrics:")
    print("Height: {}".format(health_stats[0][0]))
    print("Weight: {}".format(health_stats[0][1]))


