import datetime
def get_time_from_user(prompt):
    # acceptable time inputs
    times = ["00:00", "01:00", "02:00", "30:00", "4:00", "5:00", "6:00", "7:00", "8:00",
             "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
             "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]
    time = input(prompt)
    while time not in times:
        print("Invalid input. Format is 24h and HH:MM, all times must be on the hour (e.g 01:00, 11:00)")
        time = input(prompt)
    return time


def get_date_from_user(prompt):
    while True:
        try:
            date = input(prompt)
            datetime.datetime.strptime(date, "%Y-%m-%d")
            return date
        except Exception:
            print("Invalid date string. Format is YYYY-MM-DD")


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

def wait():
    input("Press enter to continue...")