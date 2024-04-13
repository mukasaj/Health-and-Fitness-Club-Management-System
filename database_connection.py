import psycopg

# database details
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
            # connecting to database
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
        # running login query using login details
        sql = "SELECT user_id FROM users WHERE email = %s AND password = %s"
        sql_data = (email, password,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data[0][0]
        return False

    def login_as_trainer(self, email, password):
        # running login query using login details
        sql = "SELECT trainer_id FROM trainers WHERE email = %s AND password = %s"
        sql_data = (email, password,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data[0][0]
        return False

    def login_as_admin(self, email, password):
        # running login query using login details
        sql = "SELECT email FROM admins WHERE email = %s AND password = %s"
        sql_data = (email, password,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data[0][0]
        return False

    ############################ USER RELATED FUNCTIONS ############################
    def register_user(self, email, password, first_name, last_name, date_of_birth):
        # running query to insert uesr
        sql = "INSERT INTO users (email, password, first_name, last_name, date_of_birth) VALUES (%s,%s,%s,%s,%s)"
        sql_data = (email, password, first_name, last_name, date_of_birth)
        # don't commit incase the next query fails
        if not self.execute(sql, sql_data, commit=False):
            return False
        # getting new user's id
        user_id = self.get_user_id_from_email(email)

        # icreating new users health_stats
        sql = "INSERT INTO health_stats (user_id, weight, height) VALUES (%s,%s,%s)"
        sql_data = (user_id, 0, 0)
        return self.execute(sql, sql_data, commit=True)

    def get_user_id_from_email(self, email):
        # getting user_id bemail
        sql = "SELECT user_id FROM users WHERE email = %s"
        sql_data = (email,)
        data = self.execute_select(sql, sql_data)
        return data[0][0]

    def update_user(self, user_id, email, first_name, last_name, date_of_birth):
        # updating users data
        sql = "UPDATE users SET email = %s, first_name = %s, last_name = %s, date_of_birth = %s WHERE user_id = %s"
        sql_data = (email, first_name, last_name, date_of_birth, user_id)
        return self.execute(sql, sql_data)

    def update_user_password(self, user_id, password):
        # update the password attribute for a given user_id
        sql = "UPDATE users SET password = %s WHERE user_id = %s"
        sql_data = (password, user_id)
        return self.execute(sql, sql_data)

    def get_class_list(self):
        # selecting all from classes for class list
        sql = "SELECT * FROM classes"
        return self.execute_select(sql)

    def register_for_class(self, user_id, class_id):
        # registering a user for a class through the takes table
        sql = "INSERT INTO takes(class_id, user_id) VALUES (%s, %s)"
        sql_data = (class_id, user_id)
        return self.execute(sql, sql_data)

    def get_registered_classes(self, user_id):
        # get all registered classes for user_id from takes
        sql = "SELECT classes.class_id, title, class_info, date, time FROM classes JOIN takes ON takes.class_id = classes.class_id WHERE user_id = %s"
        sql_data = (user_id,)
        return self.execute_select(sql, sql_data)

    def drop_class(self, user_id, class_id):
        # deleting entry from takes to drop class
        sql = "DELETE FROM takes WHERE user_id = %s AND class_id = %s"
        sql_data = (user_id, class_id)
        return self.execute(sql, sql_data)

    def get_fitness_goals(self, user_id):
        # getting fitness goals for given user_id
        sql = "SELECT goal FROM fitness_goals WHERE user_id = %s"
        sql_data = (user_id,)
        return self.execute_select(sql, sql_data)

    def add_fitness_goal(self, user_id, goal):
        # adding fitness goal with user_id
        sql = "INSERT INTO fitness_goals(user_id, goal) VALUES (%s, %s)"
        sql_data = (user_id, goal)
        return self.execute(sql, sql_data)

    def update_fitness_goal(self, user_id, old_goal, new_goal):
        # updating fitness goal
        sql = "UPDATE fitness_goals SET goal = %s WHERE user_id = %s AND goal = %s"
        sql_data = (new_goal, user_id, old_goal)
        return self.execute(sql, sql_data)

    def delete_fitness_goal(self, user_id, goal):
        # deletig fitness goal
        sql = "DELETE FROM fitness_goals WHERE user_id = %s AND goal = %s"
        sql_data = (user_id, goal)
        return self.execute(sql, sql_data)

    def get_health_metrics(self, user_id):
        # getting health metrics
        sql = "SELECT height, weight FROM health_stats WHERE user_id = %s"
        sql_data = (user_id,)
        return self.execute_select(sql, sql_data)

    def update_health_metrics(self, user_id, height, weight):
        # updating health metrics
        sql = "UPDATE health_stats SET height = %s, weight = %s WHERE user_id = %s"
        sql_data = (height, weight, user_id)
        return self.execute(sql, sql_data)

    def get_exercise_routines(self, user_id):
        # gettting exercise routins for give user_id
        sql = "SELECT exercise FROM exercise_routines WHERE user_id = %s"
        sql_data = (user_id,)
        return self.execute_select(sql, sql_data)

    def add_exercise_routine(self, user_id, exercise):
        # inserting exercise routine
        sql = "INSERT INTO exercise_routines (user_id, exercise) VALUES (%s, %s)"
        sql_data = (user_id, exercise)
        return self.execute(sql, sql_data)

    def update_exercise_routines(self, user_id, old_exercise, new_exercise):
        # updating exercise routine
        sql = "UPDATE exercise_routines SET exercise = %s WHERE user_id = %s AND exercise = %s"
        sql_data = (new_exercise, user_id, old_exercise)
        return self.execute(sql, sql_data)

    def delete_exercise_routine(self, user_id, exercise):
        # delete exercise routine
        sql = "DELETE FROM exercise_routines WHERE user_id = %s AND exercise = %s"
        sql_data = (user_id, exercise)
        return self.execute(sql, sql_data)

    def get_fitness_achievements(self, user_id):
        # getting fitness achievements
        sql = "SELECT achievement FROM fitness_achievements WHERE user_id = %s"
        sql_data = (user_id,)
        return self.execute_select(sql, sql_data)

    def add_fitness_achievements(self, user_id, achievement):
        # inserting fitness achievement
        sql = "INSERT INTO fitness_achievements (user_id, achievement) VALUES (%s, %s)"
        sql_data = (user_id, achievement)
        return self.execute(sql, sql_data)

    def update_fitness_achievements(self, user_id, old_achievement, new_achievement):
        # updating fitness achievement
        sql = "UPDATE fitness_achievements SET achievement = %s WHERE user_id = %s AND achievement = %s"
        sql_data = (new_achievement, user_id, old_achievement)
        return self.execute(sql, sql_data)

    def delete_fitness_achievements(self, user_id, achievement):
        # deleting fitness achievement record
        sql = "DELETE FROM fitness_achievements WHERE user_id = %s AND achievement = %s"
        sql_data = (user_id, achievement)
        return self.execute(sql, sql_data)

    def get_training_sessions(self, user_id):
        # getting training sessions
        sql = ("SELECT session_id, first_name, last_name, date, time, session_info FROM training_sessions "
               "JOIN trainers ON trainers.trainer_id = training_sessions.trainer_id WHERE user_id = %s")
        sql_data = (user_id,)
        return self.execute_select(sql, sql_data)

    def get_trainers(self):
        # getting trainers
        sql = ("SELECT trainer_id, first_name, last_name FROM trainers")
        return self.execute_select(sql)

    def get_trainer_times(self, trainer_id):
        # getting trainers available times
        sql = ("SELECT day, time FROM times WHERE trainer_id = %s")
        sql_data = (trainer_id,)
        return self.execute_select(sql, sql_data)

    def trainer_is_busy(self, trainer_id, date, time):
        # check if a trainer has a record for a given date and time, if so there is session scheduled already
        sql = ("SELECT COUNT(session_id) FROM training_sessions WHERE trainer_id = %s AND date = %s AND time = %s")
        sql_data = (trainer_id,date, time)
        data = self.execute_select(sql, sql_data)
        if data is False:
            return False
        return data[0][0] > 0

    def schedule_training_session(self, user_id, trainer_id, date, time, session_info):
        # inserting trainer session record
        sql = ("INSERT INTO training_sessions(user_id, trainer_id, date, time, session_info) VALUES (%s, %s, %s, %s, %s)")
        sql_data = (user_id, trainer_id, date, time, session_info)
        return self.execute(sql, sql_data)

    def delete_training_session(self, session_id):
        # deleting trainer session record
        sql = ("DELETE FROM training_sessions WHERE session_id = %s")
        sql_data = (session_id,)
        return self.execute(sql, sql_data)

    def get_user_bills(self, user_id):
        # selecting all bills
        sql = "SELECT * FROM bills"
        return self.execute_select(sql)

    def update_bill_status(self, user_id, bill_id, status):
        sql = "UPDATE bills SET status = %s WHERE user_id = %s AND bill_id = %s"
        sql_data = (status, user_id, bill_id)
        return self.execute(sql, sql_data)

    ############################ TRAINER RELATED FUNCTIONS ############################
    def view_available_trainer_times(self, trainer_id):
        # getting trainer's time slots
        sql = "SELECT day, time FROM times WHERE trainer_id = %s"
        sql_data = (trainer_id,)
        return self.execute_select(sql, sql_data)

    def add_available_trainer_times(self, trainer_id, day, time):
        # adding record for trainers available time
        sql = "INSERT INTO times VALUES (%s, %s, %s)"
        sql_data = (trainer_id, day, time)
        return self.execute(sql, sql_data)

    def delete_available_trainer_times(self, trainer_id, day, time):
        # deleting record of trainers available time
        sql = "DELETE FROM times WHERE trainer_id = %s AND day = %s AND time = %s"
        sql_data = (trainer_id, day, time)
        return self.execute(sql, sql_data)

    def search_user_by_name(self, first_name, last_name):

        sql = "SELECT * FROM users WHERE first_name = %s AND last_name = %s"
        sql_data = (first_name, last_name)
        return self.execute_select(sql, sql_data)

    def search_user_by_email(self, email):
        # get user record using email
        sql = "SELECT * FROM users WHERE email = %s"
        sql_data = (email,)
        return self.execute_select(sql, sql_data)

    ############################ ADMIN RELATED FUNCTIONS ############################

    def get_rooms(self):
        # getting all rooms
        sql = "SELECT * FROM rooms"
        return self.execute_select(sql)

    def get_room_bookings(self):
        # getting all room bookings
        sql = "SELECT booking_id, rooms.room_id, class_id, date, time, info, room_number FROM room_bookings JOIN rooms ON room_bookings.room_id = rooms.room_id"
        return self.execute_select(sql)


    def add_room_booking(self, room_id, class_id, date, time, info):
        # inserting room booking
        sql = "INSERT INTO room_bookings (room_id, class_id, date, time, info) VALUES (%s, %s, %s, %s, %s)"
        sql_data = (room_id, class_id, date, time, info)
        return self.execute(sql, sql_data)

    def bookings_exists(self, room_id, date, time):
        # check if room booking exists for given room_id, date, tine
        sql = "SELECT COUNT(booking_id) FROM room_bookings WHERE room_id = %s AND date = %s AND time = %s"
        sql_data = (room_id, date, time)
        data = self.execute_select(sql, sql_data)
        if data is False:
            return False
        return data[0][0] > 0


    def update_room_booking(self, booking_id, date, time):
        # update room booking
        sql = "UPDATE room_bookings SET date = %s, time = %s WHERE booking_id = %s"
        sql_data = (date, time, booking_id)
        return self.execute(sql, sql_data)

    def delete_room_booking(self, booking_id):
        # delete room booking
        sql = "DELETE FROM room_bookings WHERE booking_id = %s"
        sql_data = (booking_id,)
        return self.execute(sql, sql_data)

    def get_equipment_info(self):
        # get all equipment info
        sql = "SELECT equipment_id, equipment_info, maintenance_date, room_number FROM equipment JOIN rooms ON rooms.room_id = equipment.room_id"
        return self.execute_select(sql)


    def update_equipment_maintenance_date(self, equipment_id, maintence_date):
        # equipment maintenance date updating
        sql = "UPDATE equipment SET maintenance_date = %s WHERE equipment_id = %s"
        sql_date = (maintence_date, equipment_id)
        return self.execute_select(sql, sql_date)

    def update_class_schedule(self, class_id, date, time):
        # updating class schedule to change date and time
        sql = "UPDATE classes SET date = %s, time = %s WHERE class_id = %s"
        sql_data = (date, time, class_id)
        return self.execute(sql, sql_data)

    def get_bills(self):
        # selecting all bills
        sql = "SELECT * FROM bills"
        return self.execute_select(sql)

    def add_bill(self, user_id, date, amount, status):
        # adds bill to bills table
        sql = "INSERT INTO bills(user_id, date, amount, status) VALUES (%s, %s, %s, %s)"
        sql_data = (user_id, date, amount, status)
        return self.execute(sql, sql_data)

    ############################ EXECUTE ############################

    # used to execute sql queries in try block, used for select commands and returning data
    def execute_select(self, sql, data=None):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, data)
                data = cursor.fetchall()
                if data:
                    return data
                return False
        except Exception as e:
            print(e)
            return False

    # used to execute sql queries in try block
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
