-- select from a multiple table using join
SELECT cities.id, cities.name, state.name FROM cities INNER JOIN state ON cities.state_id = state.id ORDER BY cities.id ASC;
