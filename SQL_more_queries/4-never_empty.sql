-- 4 ID can't be null
-- Script that creates the table id_not_null on MySQL server
-- id_not_null description: id INT with the default value 1, name VARCHAR(256)
-- the database name will be passed as an argument of the mysql command
-- script should not fail if id_not_null already exists
SHOW TABLES;
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT default '1',
 );
