-- 9 Cities by States
-- Script that lists all cities contained in the database hbtn_0d_usa
-- each record should display: cities.id - cities.name - states.name
-- results must be sorted in asc order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
