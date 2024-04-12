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
        sql = "INSERT INTO users (email, password, first_name, last_name, date_of_birth) VALUES (%s,%s,%s,%s,%s)"
        sql_data = (email, password, first_name, last_name, date_of_birth)
        data = self.execute(sql, sql_data)
        return data

    def update_user(self, user_id, email, first_name, last_name, date_of_birth):
        pass

    ############################ TRAINER RELATED FUNCTIONS ############################
    def view_available_trainer_times(self, trainer_id):
        sql = "SELECT time FROM times WHERE trainer_id = %s"
        sql_data = (trainer_id,)
        data = self.execute_select(sql, sql_data)
        if data:
            return data
        return False

    def add_available_trainer_times(self, trainer_id, time):
        sql = "INSERT INTO times VALUES (%s, %s)"
        sql_data =(trainer_id, time)
        return self.execute(sql, sql_data)

    def delete_available_trainer_times(self, trainer_id, time):
        sql = "DELETE FROM times WHERE trainer_id = %s AND time = %s"
        sql_data = (trainer_id, time)
        return self.execute(sql, sql_data)

    ############################ EXECUTE ############################

    def execute_select(self, sql, data):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, data)
                return cursor.fetchall()
        except Exception as e:
            print(e)
            return False


    def execute(self, sql, data):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, data)
                self.conn.commit()
                return True
        except Exception as e:
            # rollback on failed transaction
            self.conn.rollback()
            print(e)
            return False
