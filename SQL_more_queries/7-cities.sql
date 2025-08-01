-- 7 Cities table
-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on MySQL server
-- cities description: 
-- id INT unique, auto generated, can’t be null and is a primary key,
-- state_id INT, can't be null and must be a FOREIGN KEY that references to id of the states table,
-- name VARCHAR(256) can’t be null
-- script should not fail if hbtn_d_usa already exists
-- script should not fail if cities already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS states;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
