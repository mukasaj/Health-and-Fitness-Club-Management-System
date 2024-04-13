import psycopg

DBNAME = "health_and_fitness"
USER = "postgres"
PASSWORD = "bPoz4wh-.B"
HOST = "127.0.0.1"
PORT = 5432


class DatabaseConnection:
    conn = None

    def __init__(self):
        self.__connect()

    def __connect(self):
        try:
            self.conn = psycopg.connect(
                dbname=DBNAME,
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT
            )
        except Exception as e:
            print("Failed to connect to database")
            print(e)

    ############################ LOGIN RELATED FUNCTIONS ############################
    def login_as_user(self, email, password):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        sql_data = (email, password,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data[0][0]
        return False

    def login_as_trainer(self, email, password):
        sql = "SELECT * FROM trainers WHERE email = %s AND password = %s"
        sql_data = (email, password,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data[0][0]
        return False

    def login_as_admin(self, email, password):
        sql = "SELECT * FROM admins WHERE email = %s AND password = %s"
        sql_data = (email, password,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data[0][0]
        return False

    ############################ USER RELATED FUNCTIONS ############################
    def register_user(self, email, password, first_name, last_name, date_of_birth):
        # create user
        sql = "INSERT INTO users (email, password, first_name, last_name, date_of_birth) VALUES (%s,%s,%s,%s,%s)"
        sql_data = (email, password, first_name, last_name, date_of_birth)
        if not self.execute(sql, sql_data, commit=False):
            return False

        user_id = self.get_user_id_from_email(email)

        # init health stats
        sql = "INSERT INTO health_stats (user_id, weight, height) VALUES (%s,%s,%s)"
        sql_data = (user_id, 0, 0)
        return self.execute(sql, sql_data, commit=True)

    def get_user_id_from_email(self, email):
        sql = "SELECT user_id FROM users WHERE email = %s"
        sql_data = (email,)
        data = self.execute_select(sql, sql_data)
        return data[0][0]

    def update_user(self, user_id, email, first_name, last_name, date_of_birth):
        sql = "UPDATE users SET email = %s, first_name = %s, last_name = %s, date_of_birth = %s WHERE user_id = %s"
        sql_data = (email, first_name, last_name, date_of_birth, user_id)
        return self.execute(sql, sql_data)

    def update_user_password(self, user_id, password):
        sql = "UPDATE users SET password = %s WHERE user_id = %s"
        sql_data = (password, user_id)
        return self.execute(sql, sql_data)

    def get_class_list(self):
        sql = "SELECT * FROM classes"
        return self.execute_select(sql)

    def register_for_class(self, user_id, class_id):
        sql = "INSERT INTO takes VALUES (%s, %s)"
        sql_data = (user_id, class_id)
        return self.execute(sql, sql_data)

    def get_registered_classes(self, user_id):
        sql = "SELECT classes.class_id, title, class_info, date, time FROM classes JOIN takes ON takes.class_id = classes.class_id WHERE user_id = %s"
        sql_data = (user_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    def drop_class(self, user_id, class_id):
        sql = "DELETE FROM takes WHERE user_id = %s AND class_id = %s"
        sql_data = (user_id, class_id)
        return self.execute(sql, sql_data)

    def get_fitness_goals(self, user_id):
        sql = "SELECT goal FROM fitness_goals WHERE user_id = %s"
        sql_data = (user_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    def add_fitness_goal(self, user_id, goal):
        sql = "INSERT INTO fitness_goals(user_id, goal) VALUES (%s, %s)"
        sql_data = (user_id, goal)
        return self.execute(sql, sql_data)

    def update_fitness_goal(self, user_id, old_goal, new_goal):
        sql = "UPDATE fitness_goals SET goal = %s WHERE user_id = %s AND goal = %s"
        sql_data = (new_goal, user_id, old_goal)
        return self.execute(sql, sql_data)

    def delete_fitness_goal(self, user_id, goal):
        sql = "DELETE FROM fitness_goals WHERE user_id = %s AND goal = %s"
        sql_data = (user_id, goal)
        return self.execute(sql, sql_data)

    def get_health_metrics(self, user_id):
        sql = "SELECT height, weight FROM health_stats WHERE user_id = %s"
        sql_data = (user_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    def update_health_metrics(self, user_id, height, weight):
        sql = "UPDATE health_stats SET height = %s, weight = %s WHERE user_id = %s"
        sql_data = (height, weight, user_id)
        return self.execute(sql, sql_data)

    def get_exercise_routines(self, user_id):
        sql = "SELECT exercise FROM exercise_routines WHERE user_id = %s"
        sql_data = (user_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        else:
            return False

    def add_exercise_routine(self, user_id, exercise):
        sql = "INSERT INTO exercise_routines (user_id, exercise) VALUES (%s, %s)"
        sql_data = (user_id, exercise)
        return self.execute(sql, sql_data)

    def update_exercise_routines(self, user_id, old_exercise, new_exercise):
        sql = "UPDATE exercise_routines SET exercise = %s WHERE user_id = %s AND exercise = %s"
        sql_data = (new_exercise, user_id, old_exercise)
        return self.execute(sql, sql_data)

    def delete_exercise_routine(self, user_id, exercise):
        sql = "DELETE FROM exercise_routines WHERE user_id = %s AND exercise = %s"
        sql_data = (user_id, exercise)
        return self.execute(sql, sql_data)

    def get_fitness_achievements(self, user_id):
        sql = "SELECT achievement FROM fitness_achievements WHERE user_id = %s"
        sql_data = (user_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        else:
            return False

    def add_fitness_achievements(self, user_id, achievement):
        sql = "INSERT INTO fitness_achievements (user_id, achievement) VALUES (%s, %s)"
        sql_data = (user_id, achievement)
        return self.execute(sql, sql_data)

    def update_fitness_achievements(self, user_id, old_achievement, new_achievement):
        sql = "UPDATE fitness_achievements SET achievement = %s WHERE user_id = %s AND achievement = %s"
        sql_data = (new_achievement, user_id, old_achievement)
        return self.execute(sql, sql_data)

    def delete_fitness_achievements(self, user_id, achievement):
        sql = "DELETE FROM fitness_achievements WHERE user_id = %s AND achievement = %s"
        sql_data = (user_id, achievement)
        return self.execute(sql, sql_data)

    def get_training_sessions(self, user_id):
        sql = ("SELECT session_id, first_name, last_name, date, time, session_info FROM training_sessions "
               "JOIN trainers ON trainers.trainer_id = training_sessions.trainer_id WHERE user_id = %s")
        sql_data = (user_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    def get_trainers(self):
        sql = ("SELECT trainer_id, first_name, last_name FROM trainers")
        data = self.execute_select(sql)
        if data:
            return data
        return False

    def get_trainer_times(self, trainer_id):
        sql = ("SELECT day, time FROM times WHERE trainer_id = %s")
        sql_data = (trainer_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    def trainer_is_busy(self, trainer_id, date, time):
        sql = ("SELECT COUNT(session_id) FROM training_sessions WHERE trainer_id = %s AND date = %s AND time = %s")
        sql_data = (trainer_id,date, time)
        data = self.execute_select(sql, sql_data)
        print(data)
        return data[0][0] > 0

    def schedule_training_session(self, user_id, trainer_id, date, time, session_info):
        sql = ("INSERT INTO training_sessions(user_id, trainer_id, date, time, session_info) VALUES (%s, %s, %s, %s, %s)")
        sql_data = (user_id, trainer_id, date, time, session_info)
        return self.execute(sql, sql_data)

    def delete_training_session(self, session_id):
        sql = ("DELETE FROM training_sessions WHERE session_id = %s")
        sql_data = (session_id,)
        return self.execute(sql, sql_data)

    ############################ TRAINER RELATED FUNCTIONS ############################
    def view_available_trainer_times(self, trainer_id):
        sql = "SELECT day, time FROM times WHERE trainer_id = %s"
        sql_data = (trainer_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    def add_available_trainer_times(self, trainer_id, day, time):
        sql = "INSERT INTO times VALUES (%s, %s, %s)"
        sql_data = (trainer_id, day, time)
        return self.execute(sql, sql_data)

    def delete_available_trainer_times(self, trainer_id, day, time):
        sql = "DELETE FROM times WHERE trainer_id = %s AND day = %s AND time = %s"
        sql_data = (trainer_id, day, time)
        return self.execute(sql, sql_data)

    def search_user_by_name(self, first_name, last_name):
        sql = "SELECT * FROM users WHERE first_name = %s AND last_name = %s"
        sql_data = (first_name, last_name)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    def search_user_by_email(self, email):
        sql = "SELECT * FROM users WHERE email = %s"
        sql_data = (email,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    ############################ ADMIN RELATED FUNCTIONS ############################

    def get_rooms(self):
        sql = "SELECT * FROM rooms"
        data = self.execute_select(sql)
        if data:
            return data
        return False
    def get_room_bookings(self):
        sql = "SELECT * FROM room_bookings"
        data = self.execute_select(sql)
        if data:
            return data
        return False

    def add_room_booking(self, room_id, class_id, date, time, info):
        sql = "INSERT INTO room_bookings (room_id, class_id, date, time, info) VALUES (%s, %s, %s, %s, %s)"
        sql_data = (room_id, class_id, date, time, info)
        return self.execute(sql, sql_data)

    def bookings_exists(self, room_id, date, time):
        sql = "SELECT COUNT(booking_id) FROM room_bookings WHERE room_id = %s AND date = %s AND time = %s"
        sql_data = (room_id, date, time)
        data = self.execute_select(sql, sql_data)
        return data[0][0] > 0


    def update_room_booking(self, booking_id, date, time):
        sql = "UPDATE room_bookings SET date = %s, time = %s WHERE booking_id = %s"
        sql_data = (date, time, booking_id)
        return self.execute(sql, sql_data)

    def delete_room_booking(self, booking_id):
        sql = "DELETE FROM room_bookings WHERE booking_id = %s"
        sql_data = (booking_id,)
        return self.execute(sql, sql_data)

    def get_equipment_info(self):
        sql = "SELECT * FROM equipment"
        data = self.execute_select(sql)
        if data:
            return data
        return False

    def update_equipment_maintanance_date(self, equipment_id, maintence_date):
        sql = "UPDATE equipment SET maintenance_date = %s WHERE equipment_id = %s"
        sql_date = (maintence_date, equipment_id)
        return self.execute_select(sql, sql_date)

    def update_class_schedule(self, class_id, date, time):
        sql = "UPDATE classes SET date = %s, time = %s WHERE class_id = %s"
        sql_data = (date, time, class_id)
        return self.execute(sql, sql_data)

    def get_bills(self):
        sql = "SELECT * FROM bills"
        data = self.execute_select(sql)
        if data:
            return data
        else:
            False

    def add_bill(self, user_id, date, amount, status):
        sql = "INSERT INTO bills(user_id, date, amount, status) VALUES (%s, %s, %s, %s)"
        sql_data = (user_id, date, amount, status)
        return self.execute(sql, sql_data)

    ############################ EXECUTE ############################

    def execute_select(self, sql, data=None):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, data)
                return cursor.fetchall()
        except Exception as e:
            print(e)
            return False

    def execute(self, sql, data, commit=True):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, data)
                if commit:
                    self.conn.commit()
                return True
        except Exception as e:
            # rollback on failed transaction
            self.conn.rollback()
            print(e)
            return False
