-- 16 Say my name
-- Script that lists all records of the table second_table of the 
-- database hbtn_0c_0 in my MySQL server
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC, name;
