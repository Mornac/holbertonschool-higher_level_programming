-- States table
-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on MySQL server
-- states description: id INT unique, auto generated, can’t be null and is a primary key, name VARCHAR(256) can’t be null
-- script should not fail if hbtn_d_usa already exists
-- script should not fail if states already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
DROP TABLE IF EXISTS states;
CREATE TABLE states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
