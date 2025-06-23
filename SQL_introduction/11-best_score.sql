-- 11 Select the best
-- Script that lists all records with a score >= 10 in second_table table of hbtn_0c_0 database
-- in my MySQL server.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC, name;
