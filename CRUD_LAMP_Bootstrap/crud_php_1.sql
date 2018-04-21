-- Copyright (C) 2017-2018 Jamil Said Jr 

CREATE DATABASE phpCrud;

USE phpCrud;

CREATE TABLE  `Customers` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    `firstName` VARCHAR( 255 ) NOT NULL ,
    `lastName` VARCHAR( 255 ) NOT NULL ,
    `email` VARCHAR( 100 ) NOT NULL ,
    `phone` VARCHAR( 30 ) NOT NULL ,
    `created` TIMESTAMP NOT NULL DEFAULT NOW() , 
    `modified` TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW()
) ENGINE = INNODB;
