-- 15 Number by score
-- Script that lists the number of records with the same score
-- in the second_table table of database hbtn_0c_0 in my MySQL server
SELECT score, count(*) as 'number' FROM second_table GROUP BY score ORDER BY score DESC;
