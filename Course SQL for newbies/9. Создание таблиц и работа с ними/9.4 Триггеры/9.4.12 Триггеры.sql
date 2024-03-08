DROP TABLE IF EXISTS Users;
CREATE TABLE Users
(
    id           INT AUTO_INCREMENT,
    name         VARCHAR(20),
    surname      VARCHAR(20),
    phone_number VARCHAR(20),
    PRIMARY KEY (id)
);

INSERT INTO Users (name, surname, phone_number)
VALUES ('Matt', 'Damon', '+79087333025'),
       ('Edward', 'Norton', '+79642218964'),
       ('Nicolas', 'Cage', '+79808814813'),
       ('Ben', 'Affleck', '+79042778299'),
       ('John', 'Travolta', '+79640950623');

