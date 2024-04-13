CREATE TABLE rooms(
    room_id SERIAL PRIMARY KEY,
    room_number INT UNIQUE NOT NULL
);
CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(75) UNIQUE NOT NULL,
    password varchar(50) NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    date_of_birth DATE NOT NULL
);
CREATE TABLE trainers(
    trainer_id SERIAL PRIMARY KEY,
    email VARCHAR(75) NOT NULL,
    password VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);
CREATE TABLE admins(
    email VARCHAR(64) PRIMARY KEY,
    password VARCHAR(50) NOT NULL
);
CREATE TABLE classes(
    class_id SERIAL PRIMARY KEY,
    title VARCHAR(75) NOT NULL,
    class_info TEXT,
    date DATE NOT NULL,
    time TIME NOT NULL
);
CREATE TABLE equipment(
    equipment_id SERIAL PRIMARY KEY,
    room_id SERIAL,
    equipment_info TEXT NOT NULL,
    maintenance_date DATE,
    FOREIGN KEY (room_id)
        REFERENCES rooms(room_id)
);
CREATE TABLE times(
    trainer_id SERIAL NOT NULL,
    day varchar(10) NOT NULL,
    time TIME NOT NULL,
    PRIMARY KEY (trainer_id, day, time),
    FOREIGN KEY (trainer_id)
        REFERENCES trainers(trainer_id)
);
CREATE TABLE training_sessions(
    session_id SERIAL PRIMARY KEY,
    user_id SERIAL NOT NULL,
    trainer_id SERIAL NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    session_info TEXT,
    FOREIGN KEY (user_id)
        REFERENCES users(user_id),
    FOREIGN KEY (trainer_id)
        REFERENCES trainers(trainer_id)
);
CREATE TABLE takes(
    class_id SERIAL NOT NULL,
    user_id SERIAL NOT NULL,
    PRIMARY KEY (class_id, user_id),
    FOREIGN KEY (class_id)
        REFERENCES classes(class_id),
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
CREATE TABLE room_bookings(
    booking_id SERIAL PRIMARY KEY,
    room_id SERIAL NOT NULL,
    class_id INT,
    date DATE NOT NULL,
    time TIME NOT NULL,
    info text NOT NULL,
    FOREIGN KEY (room_id)
        REFERENCES rooms(room_id),
    FOREIGN KEY (class_id)
        REFERENCES classes(class_id)
);
CREATE TABLE health_stats(
    user_id SERIAL PRIMARY KEY,
    weight INT,
    height INT,
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
CREATE TABLE fitness_goals(
    user_id SERIAL NOT NULL,
    goal TEXT NOT NULL,
    PRIMARY KEY (user_id, goal),
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
CREATE TABLE fitness_achievements(
    user_id SERIAL NOT NULL,
    achievement TEXT NOT NULL,
    PRIMARY KEY (user_id, achievement),
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
CREATE TABLE exercise_routines(
    user_id SERIAL NOT NULL,
    exercise TEXT NOT NULL,
    PRIMARY KEY (user_id, exercise),
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
CREATE TABLE bills(
    bill_id SERIAL PRIMARY KEY,
    user_id SERIAL NOT NULL,
    date DATE NOT NULL,
    amount NUMERIC(5,2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
