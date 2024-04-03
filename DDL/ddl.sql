CREATE TABLE admins(
    id  SERIAL  PRIMARY KEY,
    username varchar(32) UNIQUE NOT NULL,
    password varchar(32) NOT NULL,

);

CREATE TABLE trainers(
    id  SERIAL  PRIMARY KEY,
    username varchar(32) UNIQUE NOT NULL,
    password varchar(32) NOT NULL,
    firstname varchar(32) NOT NULL,
    lastname varchar(32) NOT NULL,
);

CREATE TABLE users(
    id  SERIAL  PRIMARY KEY,
    username varchar(32) UNIQUE NOT NULL,
    password varchar(32) NOT NULL,
    firstname varchar(32) NOT NULL,
    lastname varchar(32) NOT NULL,
);

CREATE TABLE health_statistics(
    id SERIAL PRIMARY KEY,
    user_id NOT NULL,
    weight NUMERIC(3,1),
    height NUMERIC(3,1)

    user_id FOREIGN KEY
        REFERENCES users(id)
)

