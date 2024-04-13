################################### PRINTING FUNCTIONS ###################################
from datetime import datetime


def print_goals(goals):
    goal_index = 0
    if goals:
        for goal in goals:
            print("{}: Goal: {}".format(goal_index, goal[0]))
            goal_index += 1


def print_exercise_routines(exercises):
    exercise_index = 0
    for exercise in exercises:
        print("{}: Exercise Routine: {}".format(exercise_index, exercise[0]))
        exercise_index += 1


def print_fitness_achievements(achievements):
    achievement_index = 0
    for achievement in achievements:
        print("{}: Achievement: {}".format(achievement_index, achievement[0]))
        achievement_index += 1

def print_training_sessions(sessions):
    session_index = 0
    for session in sessions:
        print("{}: Trainer: {} {},\tDate: {},\tTime: {},\tInfo: {}".
              format(session_index,
                     session[1],
                     session[2],
                     session[3].strftime("%Y-%m-%d"),
                     session[4].strftime("%H:%M"),
                     session[5]
                     ))
        session_index += 1

def print_trainer_schedule(times):
    time_index = 0
    print("Times:")
    for time in times:
        print("{}: Day: {}, Time: {}".format(time_index, time[0], time[1].strftime("%H:%M")))
        time_index += 1


def print_rooms(rooms):
    room_index = 0
    for room in rooms:
        print("{}: Room Number: {}".format(room_index, room[1]))
        room_index += 1


def print_equipment(equipment):
    equipment_index = 0
    for equip in equipment:
        print("{}: Info: {}\tRoom Number: {}\tMaintenance Date: {}".
              format(equipment_index,
                     equip[1],
                     equip[3],
                     equip[2].strftime("%Y-%m-%d")
                     ))
        equipment_index += 1


def print_classes(classes):
    class_index = 0
    for a_class in classes:
        print("{}: Title: {},\tDesc: {},\tDate: {},\tTime: {}".
              format(class_index,
                        a_class[1],
                        a_class[2],
                        a_class[3].strftime("%Y-%m-%d"),
                        a_class[4].strftime("%H:%M")
                     ))
        class_index += 1


def print_bookings(bookings):
    booking_index = 0
    for booking in bookings:
        print("{}: Room Number: {},\tClass: {},\tDate: {},\tTime: {},\tInfo: {}".
              format(booking_index,
                    booking[6],
                    booking[2],
                    booking[3].strftime("%Y-%m-%d"),
                    booking[4].strftime("%H:%M"),
                    booking[5]))
        booking_index += 1


def print_bills(bills):
    bill_index = 0
    for bill in bills:
        print("{}: Date issued: {},\tAmount: {},\tStatus: {}".
              format(bill_index, bill[2].strftime("%Y-%m-%d"), bill[3], bill[4]))
        bill_index += 1
