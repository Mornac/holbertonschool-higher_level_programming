-- 3 Always a name
-- Script that creates the table force_name on MySQL server
-- force_name description: id INT, name VARCHAR(256) can't be null
-- database name will be passed as an argument of mysql command
-- script should not fail if force_name already exists
SHOW TABLES;
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
