-- 1 Root user
-- Script that creates the MySQL server user user_0d_1
-- user_0d_1 should have all privileges on MySQL server
-- user_0d_1 password shoult be set to user_0d_1_pwd
-- script should not fail if user_0d_1 already exists
DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
