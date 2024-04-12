CREATE TABLE rooms(
    room_id SERIAL PRIMARY KEY,
    room_number INT UNIQUE NOT NULL,
    capacity INT NOT NULL
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
    room_id SERIAL NOT NULL,
    title VARCHAR(75) NOT NULL,
    class_info TEXT,
    date DATE NOT NULL,
    time TIME NOT NULL,
    FOREIGN KEY (room_id)
        REFERENCES rooms(room_id)
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
    time TIME NOT NULL,
    PRIMARY KEY (trainer_id, time),
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
CREATE TABLE health_stats(
    user_id SERIAL PRIMARY KEY,
    weight INT,
    height INT,
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
CREATE TABLE fitness_goals(
    user_id SERIAL PRIMARY KEY,
    goal TEXT NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
CREATE TABLE fitness_achievements(
    user_id SERIAL PRIMARY KEY,
    achievement TEXT NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);
CREATE TABLE exercise_routine(
    user_id SERIAL PRIMARY KEY,
    exercise TEXT NOT NULL,
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
