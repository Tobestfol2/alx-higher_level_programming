-- This script lists all cities of California that can be found in the database hbtn_0d_usa.
-- Results is sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The database name will passed as an argument of the mysql command

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California')ORDER BY id;
