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
    # get times and print
    times = conn.view_available_trainer_times(trainer_id)
    if (times):
        p.print_trainer_schedule(times)
    else:
        print("No times set")


def add_timeslot(trainer_id):
    # insert time slot
    day = input("Please enter the day: ")
    time = input("Please enter time slot(HH in 24h format): ")
    if (conn.add_available_trainer_times(trainer_id, day, time)):
        print("Time slot added")
    else:
        print("Failed to add time slot")


def delete_timeslot(trainer_id):
    # get current times
    times = conn.view_available_trainer_times(trainer_id)
    if (times):
        p.print_trainer_schedule(times)
    else:
        print("No times set")
        return

    # select time to delete
    times_index = s.get_int("Enter the index of the time slot you wish to delete: ")
    if (times_index is None) or (not (0 <= times_index < len(times))):
        print("invalid index")
        return

    # delete time
    if (conn.delete_available_trainer_times(trainer_id, times[times_index][0], times[times_index][1])):
        print("Time slot deleted")
    else:
        print("Failed to delete time slot")

def get_user_by_name():
    # get user by name and print their dashboard
    first_name = input("Please enter the user's first name: ")
    last_name = input("Please enter the user's last name: ")
    data = conn.search_user_by_name(first_name, last_name)
    if data:
        get_user_dashboard(data[0][0])
    else:
        print("No user found")
        return

def get_user_by_email():
    # get user by email and print their dashboard
    email = input("Please enter the user's email: ")
    data = conn.search_user_by_email(email)
    if data:
        get_user_dashboard(data[0][0])
    else:
        print("No user found")
        return

def get_user_dashboard(user_id):
    # get dashboard info
    exercises = conn.get_exercise_routines(user_id)
    achievements = conn.get_fitness_achievements(user_id)
    health_stats = conn.get_health_metrics(user_id)

    # print dashboard
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
    print("\nUser's health metrics:")
    print('Height: {}"'.format(health_stats[0][0]))
    print("Weight: {}lbs".format(health_stats[0][1]))


