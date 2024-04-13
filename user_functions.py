import datetime
from database_connection import DatabaseConnection
import print_functions as p
import support_functions as s

# database connection object
conn = DatabaseConnection()

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

def user_login():
    print("User Login")
    email = input("Email: ")
    password = input("Password: ")
    return conn.login_as_user(email, password)

def update_personal_information(user_id):
    print("Please enter your personal information")
    email = input("Email: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    date_of_birth = s.get_date_from_user("Date of birth(yyyy-mm-dd): ")
    if conn.update_user(user_id, email, first_name, last_name, date_of_birth):
        print("Successfully updated personal information")
    else:
        print("Failed to update personal information")


def update_user_password(user_id):
    print("Please enter your new password")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    while password != confirm_password:
        print("Passwords do not match")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")
    conn.update_user_password(user_id, password)

def view_goals(user_id):
    goals = conn.get_fitness_goals(user_id)
    if goals:
        p.print_goals(goals)
    else:
        print("You have no fitness goals")

def add_user_goal(user_id):
    goal = input("Please enter your goal: ")
    if conn.add_fitness_goal(user_id, goal):
        print("Successfully added fitness goal")
    else:
        print("Failed to add fitness goal")


def update_user_goal(user_id):
    goals = conn.get_fitness_goals(user_id)
    if goals:
        p.print_goals(goals)
    else:
        print("You have no fitness goals")
        return
    index_to_delete = int(input("Enter the index of the goal you want to update: "))
    new_goal = input("Please enter your new goal: ")
    old_goal = goals[index_to_delete][0]
    if conn.update_fitness_goal(user_id, old_goal, new_goal):
        print("Goal successfully updated")
    else:
        print("Failed to update goal")


def delete_user_goal(user_id):
    goals = conn.get_fitness_goals(user_id)
    if goals:
        p.print_goals(goals)
    else:
        print("You have no fitness goals")
        return
    index_to_delete = int(input("Enter the index of the goal you want to delete: "))
    goal = goals[index_to_delete][0]
    if conn.delete_fitness_goal(user_id, goal):
        print("Goal successfully deleted")
    else:
        print("Failed to delete goal")

def view_health_metrics(user_id):
    print("Health metrics:")
    metrics = conn.get_health_metrics(user_id)
    if metrics:
        for metric in metrics:
            print("Height: {}, Weight: {}".format(metric[0], metric[1]))
    else:
        print("You have no health metrics")

def update_user_metric(user_id):
    height = input("Height: ")
    weight = input("Weight: ")
    if conn.update_health_metrics(user_id, height, weight):
        print("Successfully updated health metrics")
    else:
        print("Failed to update health metrics")

def view_exercise_routines(user_id):
    exercises = conn.get_exercise_routines(user_id)
    if exercises:
        p.print_exercise_routines(exercises)
    else:
        print("You have no exercise routines")
def add_exercise_routine(user_id):
    exercises = input("Enter exercise routine: ")
    if conn.add_exercise_routine(user_id, exercises):
        print("Added exercise routine")
    else:
        print("Failed to add exercise routine")

def update_exercise_routine(user_id):
    exercises = conn.get_exercise_routines(user_id)
    if exercises:
        p.print_exercise_routines(exercises)
    else:
        print("You have no exercise routines")
        return
    exercises_index = int(input("Enter exercise index you wish to update: "))
    old_exercise = exercises[exercises_index][0]
    new_exercise = input("Enter updated exercise: ")
    if conn.update_exercise_routines(user_id, old_exercise, new_exercise):
        print("Exercise routine successfully updated")
    else:
        print("Failed to update exercise routine")

def delete_exercise_routine(user_id):
    exercises = conn.get_exercise_routines(user_id)
    if exercises:
        p.print_exercise_routines(exercises)
    else:
        print("You have no exercise routines")
        return
    exercises_index = int(input("Enter exercise index you wish to delete: "))
    exercise = exercises[exercises_index][0]
    if conn.delete_exercise_routine(user_id, exercise):
        print("Exercise routine successfully deleted")
    else:
        print("Failed to delete exercise routine")

def view_achievements(user_id):
    achievements = conn.get_fitness_achievements(user_id)
    if achievements:
        p.print_fitness_achievements(achievements)
    else:
        print("You have no fitness achievements")
def add_achievement(user_id):
    achievement = input("Enter fitness achievement routine: ")
    if conn.add_fitness_achievements(user_id, achievement):
        print("Fitness achievement successfully added")
    else:
        print("Failed to add fitness achievement")
def update_achievement(user_id):
    achievement = conn.get_fitness_achievements(user_id)
    if achievement:
        p.print_fitness_achievements(achievement)
    else:
        print("You have no fitness achievements")
        return
    achievement_index = int(input("Enter achievement index you wish to update: "))
    old_achievement = achievement[achievement_index][0]
    new_achievement = input("Enter updated achievement: ")
    if conn.update_fitness_achievements(user_id, old_achievement, new_achievement):
        print("Fitness achievement successfully updated!")
    else:
        print("Failed to update fitness achievement")
def delete_achievement(user_id):
    exercises = conn.get_fitness_achievements(user_id)
    if exercises:
        p.print_fitness_achievements(exercises)
    else:
        print("You have no fitness achievements")
        return
    exercises_index = int(input("Enter achievement index you wish to delete: "))
    exercise = exercises[exercises_index][0]
    if conn.delete_exercise_routine(user_id, exercise):
        print("Fitness achievement successfully deleted")
    else:
        print("Failed to delete fitness achievement")
def dashboard(user_id):
    exercises = conn.get_exercise_routines(user_id)
    achievements = conn.get_fitness_achievements(user_id)
    health_stats = conn.get_health_metrics(user_id)

    print("DASHBOARD:")
    print("Your exercises are:")
    if exercises:
        p.print_exercise_routines(exercises)
    else:
        print("No exercises found")
    print("\nYour achievements are:")
    if achievements:
        p.print_fitness_achievements(achievements)
    else:
        print("No achievements found")
    print("\nYour health metrics:")
    print('Height: {}"'.format(health_stats[0][0]))
    print("Weight: {}lbs".format(health_stats[0][1]))

def view_training_sessions(user_id):
    sessions = conn.get_training_sessions(user_id)
    if sessions:
        p.print_training_sessions(sessions)
    else:
        print("You have no training sessions scheduled")
def schedule_training_session(user_id):
    trainers = conn.get_trainers();

    trainer_index = 0
    if trainers:
        print("Trainers:")
        for trainer in trainers:
            print(f"{trainer_index}: {trainer[1]} {trainer[2]}")
            trainer_index += 1
    else:
        print("No trainers")
        return

    selected_trainer = int(input("Please into the index of the trainer you'd like to book a session with: "))

    trainer_id = trainers[selected_trainer][0]
    times = conn.get_trainer_times(trainer_id)
    if times:
        print("This trainer is available at these times")
        for time in times:
            print(f"Day: {time[0]} - Time: {time[1]}")
    else:
        print("This trainer has no times available")
        return

    date = s.get_date_from_user("Please enter you session date: ")
    time = s.get_time_from_user("Please enter you session time: ")
    weekday = s.map_python_weekday_to_string(datetime.datetime.strptime(date, "%Y-%m-%d").weekday())
    mapped_time = datetime.datetime.strptime(time, '%H:%M').time()
    if (str(weekday).upper(), mapped_time) not in times:
        print(f"This trainer is not available at {time} on {weekday}")
        return

    if conn.trainer_is_busy(trainer_id, date, time):
        print(f"This trainer is not available at {time} on {date}")
        return

    session_info = input("Please enter the session info: ")
    if conn.schedule_training_session(user_id, trainer_id, date, time, session_info):
        print("Successfully scheduled training session")
    else:
        print("Failed to schedule training session")

def cancel_training_session(user_id):
    sessions = conn.get_training_sessions(user_id)
    if sessions:
        p.print_training_sessions(sessions)
    else:
        print("You have no training sessions scheduled")
        return
    session_index = int(input("Enter session index you wish to delete: "))
    session_id = sessions[session_index][0]

    if conn.delete_training_session(session_id):
        print("Successfully canceled training session")
    else:
        print("Failed to canceled training session")

def view_classes(user_id):
    classes = conn.get_registered_classes(user_id)
    if classes:
        p.print_classes(classes)
    else:
        print("You are not registered for any classes.")

def register_for_class(user_id):
    # printing classes available for registration
    print("Available classes:")
    classes = conn.get_class_list()
    if classes:
        p.print_classes(classes)
    else:
        print("No classes available.")
    class_index = int(input("Enter the class index: "))
    if conn.register_for_class(user_id, classes[class_index][0]):
        print("Successfully registered for class")
    else:
        print("Failed to register for class")
def drop_class(user_id):
    classes = conn.get_registered_classes(user_id)
    if classes:
        p.print_classes(classes)
    else:
        print("You are not registered for any classes.")
        return
    class_index = int(input("Enter the class index: "))
    if conn.drop_class(user_id, classes[class_index][0]):
        print("Successfully dropped class")
    else:
        print("Failed to drop class")

def view_bills(user_id):
    bills = conn.get_user_bills(user_id)
    if bills:
        p.print_bills(bills)
    else:
        print("No bills")

def pay_bill(user_id):
    view_bills(user_id)

    bills = conn.get_bills()
    bills_index = int(input("Enter the index to pay: "))
    bill_id = bills[bills_index][0]

    # payment processor would go here, just setting status
    status = "PAID"
    input("Press Enter to pay bill...")

    if conn.update_bill_status(user_id, bill_id, status):
        print("Bill successfully paid")
    else:
        print("Failed to pay bill")