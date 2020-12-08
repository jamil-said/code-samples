-- Database creation for Flask-Python3-MySQL CRUD API:

-- Creation of Database and suitable DB user (Important: create user with mysql_native_password on MySQL 8.0+)
-- mysql -u root -p (run this in shell first)
CREATE DATABASE FlaskP3Api;
CREATE USER 'flaskapiuser'@'localhost' IDENTIFIED WITH mysql_native_password BY '12WWdsff!er3SSd8Yz3KK!c?aerwfsvVa22';
GRANT ALL PRIVILEGES ON *.* TO 'flaskapiuser'@'localhost';
FLUSH PRIVILEGES;
USE FlaskP3Api;

-- Creating main apiusers table
CREATE TABLE apiusers (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    UNIQUE KEY unique_email (email)
) ENGINE = INNODB;


-- seeding some records on database
INSERT INTO apiusers (first_name, last_name, email, created_at, updated_at) VALUES
    ('Joe', 'Carlo', 'jcar1122@gmail.com', utc_timestamp(), utc_timestamp()),
    ('Louis', 'Bonter', 'bonty32@outlook.com', utc_timestamp(), utc_timestamp()),
    ('Laurel', 'Yang', 'ly@yahoo.com', utc_timestamp(), utc_timestamp());
