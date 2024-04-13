INSERT INTO users(email, password, first_name, last_name, date_of_birth)
VALUES
('jane@gmail.com', 'jane', 'Jane', 'Doe', '1999-01-01'),
('jim@gmail.com', 'jim', 'Jim', 'Smith', '1994-03-28'),
('john@gmail.com', 'john', 'John', 'Jackson', '2001-02-12'),
('sarah@gmail.com', 'sarah', 'Sarah', 'Cook', '2002-11-01');

INSERT INTO health_stats(user_id, weight, height)
VALUES
(1, 0, 0),
(2, 0, 0),
(3, 0, 0),
(4, 0, 0);

INSERT INTO trainers(email, password, first_name, last_name)
VALUES
('tim@fitness.com', 'tim', 'Tim', 'Doe'),
('kyle@fitness.com', 'kyle', 'Kyle', 'Smith'),
('abby@fitness.com', 'abby', 'Abby', 'Jackson'),
('sam@fitness.com', 'sam', 'Sam', 'Cook');

INSERT INTO times(trainer_id, day, time)
VALUES
(1, 'MONDAY', '12:00'),
(1, 'MONDAY', '13:00'),
(2, 'TUESDAY', '14:00'),
(2, 'TUESDAY', '15:00'),
(3, 'FRIDAY', '13:00'),
(3, 'FRIDAY', '14:00'),
(4, 'SUNDAY', '10:00'),
(4, 'SUNDAY', '11:00');

INSERT into rooms(room_number)
VALUES
(101),
(102),
(103),
(104);

INSERT INTO equipment(room_id, equipment_info, maintenance_date)
VALUES
(1, 'bike', '2024-08-20'),
(1, 'bike', '2024-08-20'),
(1, 'bike', '2024-08-20'),
(1, 'bike', '2024-08-20'),
(2, 'treadmill', '2024-05-25'),
(2, 'treadmill', '2024-05-25'),
(2, 'treadmill', '2024-05-25'),
(2, 'treadmill', '2024-05-25'),
(3, 'stepper', '2024-07-05'),
(3, 'stepper', '2024-07-05'),
(3, 'stepper', '2024-07-05'),
(3, 'stepper', '2024-07-05'),
(4, 'elliptical', '2024-11-10'),
(4, 'elliptical', '2024-11-10'),
(4, 'elliptical', '2024-11-10'),
(4, 'elliptical', '2024-11-10');

INSERT INTO classes(title, class_info, date, time)
VALUES
('Cycling class', 'Learn proper cycling technique', '2024-04-15', '14:00'),
('Running class', 'Learn proper running technique', '2024-04-17', '13:00'),
('Stepper class', 'Come get your sweat on', '2024-04-18', '15:00'),
('Elliptical class', 'Come get your sweat on', '2024-04-20', '12:00');

INSERT INTO admins(email, password)
VALUES
('justin@fitness.com', 'justin'),
('paul@fitness.com', 'paul'),
('hailey@fitness.com', 'hailey');