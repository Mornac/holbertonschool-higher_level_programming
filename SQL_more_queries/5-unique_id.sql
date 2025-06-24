-- 5 Unique ID
-- Script that creates the table unique_id on MySQL server
-- unique_id description: id INT with the default value 1 and must be unique, name VARCHAR(256)
-- the database name will be passed as an argument of the mysql command
-- script should not fail if unique_id already exists
SHOW TABLES;
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT DEFAULT '1' UNIQUE,
    `name` VARCHAR(256)
);
