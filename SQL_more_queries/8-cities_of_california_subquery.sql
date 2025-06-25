-- 8 Cities of California
-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- states table contains only 1 record where name = California (but the id can be different)
-- results must be sorted in ascending order by cities.id
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name ='California');
