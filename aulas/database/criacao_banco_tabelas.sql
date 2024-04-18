CREATE DATABASE `dio_db`;

USE dio_db;

CREATE TABLE `Users` (
    `id` int  NOT NULL AUTO_INCREMENT,
    `name` varchar(255)  NOT NULL COMMENT 'User name.',
    `email` varchar(100) NOT NULL UNIQUE COMMENT 'User e-mail',
    `birthDate` Date  NOT NULL COMMENT 'User birthdate',
    `address` varchar(100)  NOT NULL COMMENT 'User address',
    PRIMARY KEY (
        `id`
    )
);



CREATE TABLE `Reservations` (
    `id` int  NOT NULL AUTO_INCREMENT,
    `user_id` int  NOT NULL COMMENT 'Reference to user id that make a reservation',
    `destiny_id` int  NOT NULL COMMENT 'Reference to destiny id',
    `date` datetime COMMENT 'Date of creation of the reserve',
    `status` varchar(255)  NOT NULL default 'pendente' COMMENT 'Status of reservation (created, pending, canceled, etc.)',
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `Destiny` (
    `id` int  NOT NULL AUTO_INCREMENT,
    `name` varchar(50)  NOT NULL COMMENT 'Destiny name',
    `description` varchar(50)  NOT NULL COMMENT 'Destiny description',
    PRIMARY KEY (
        `id`
    )
);

ALTER TABLE `Reservations` ADD CONSTRAINT `fk_Reservations_user_id` FOREIGN KEY(`user_id`)
REFERENCES `Users` (`id`);

ALTER TABLE `Reservations` ADD CONSTRAINT `fk_Reservations_destiny_id` FOREIGN KEY(`destiny_id`)
REFERENCES `Destiny` (`id`);
