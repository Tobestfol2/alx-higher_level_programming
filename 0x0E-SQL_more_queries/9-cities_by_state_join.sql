-- This script lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id
-- One can use only one SELECT statement
-- The database name is passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states WHERE cities.state_id=states.id
