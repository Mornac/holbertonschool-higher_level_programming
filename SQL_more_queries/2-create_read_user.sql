-- 2 Read user
-- Script that creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 password should be set to user_0d_2_pwd
-- script should not fail if the database hbtn_0d_2 already exists
-- script should not fail if the user user_0d_2 already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
